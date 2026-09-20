using UnityEngine;
using UnityEngine.UI;

public class PlayerController : MonoBehaviour
{
    public CheckAnimation Animation;

    public PauseManager Pause;

    public enum RunState
    {
        Running,
        Braking,
        Stopped,
        Accelerating
    }

    [Header("Run State")]
    public RunState runState = RunState.Running;

    [Header("Brake Settings")]
    private float currentBrakeDeceleration;
    public float brakeSpeed = 4f; //ความเร็วในการลดความเร็ว
    public float accelerationSpeed = 4f; //ความเร็วในการเร่งกลับ
    public float stopDistance = 0.05f; //ระยะที่ถือว่าถึงจุดหยุดแล้ว

    private Transform currentStopPoint; //จุดที่ต้องหยุด
    private GameObject targetMinigameCamera; //กล้องมินิเกมที่จะเปิดเมื่อหยุดแล้ว

    public float Timer = 0f;
    public float DelayTime = 1f;

    [Header("Fast Fall")]
    public float fastFallSpeed = 20f;
    public float fastFallBoost = 5f;

    public float boostRecoverySpeed = 3f;

    private float currentMoveSpeed;

    [Header("Speed")]
    public float speed = 5f; // ความเร็วพื้นฐานปัจจุบัน
    public float maxSpeed = 8f; // ความเร็วสูงสุด
    public float speedIncreaseRate = 0.05f; // เพิ่มความเร็วต่อวินาที
    [Header("Jump")]
    public float jumpForce = 7f;
    [Header("Checkwall")]
    public float speedwallcheck = 2;

    public Rigidbody rb;

    public Transform groundCheck;
    public Transform wallCheck;
    public Transform wallCheck2;
    public float groundDistance = 0.3f;
    public float wallDistance = 0.3f;
    public LayerMask groundLayer;

    public GameObject checkSelfActive;

    public bool isGrounded;
    public bool isGroundedright;
    public bool isGroundedright2;

    public bool miniGame1;
    public bool canJump;
    public bool canSlice;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
        checkSelfActive.SetActive(true);

        canJump = true;
        canSlice = true;

    currentMoveSpeed = speed;

    }

    void Update()
    {

        // ตรวจว่าติดผนังขวาไหม
        isGroundedright = Physics.Raycast(wallCheck.position, Vector3.right, wallDistance, groundLayer);

        isGroundedright2 = Physics.Raycast(wallCheck2.position, Vector3.right, wallDistance, groundLayer);

        // ตรวจว่าติดพื้นไหม
        isGrounded = Physics.Raycast(groundCheck.position, Vector3.down, groundDistance, groundLayer);


        // เช็คว่าติดผนังขวาไหม ถ้าติดให้วิ่งช้าลง
        if (isGroundedright)
        {
            rb.linearVelocity = new Vector3(speedwallcheck, rb.linearVelocity.y, 0);
        }

        if (isGroundedright2)
        {
            rb.linearVelocity = new Vector3(speedwallcheck, rb.linearVelocity.y, 0);
        }

        // เพิ่มความเร็วพื้นฐานเรื่อย ๆ เฉพาะตอนวิ่งปกติ
        if (runState == RunState.Running)
        {
            speed = Mathf.MoveTowards(
                speed,
                maxSpeed,
                speedIncreaseRate * Time.deltaTime
            );
        }

        // กระโดด
        if (Input.GetKeyDown(KeyCode.Space) && (isGrounded || isGroundedright) && runState != RunState.Stopped && canJump)//Player จะไม่กระโดดระหว่างเปิดมินิเกม
        {
            rb.AddForce(Vector3.up * jumpForce, ForceMode.Impulse);
        }

        if ((Input.GetKeyDown(KeyCode.S) || Input.GetKeyDown(KeyCode.DownArrow)) && !isGrounded && canSlice)
        {
            // เพิ่มความเร็วไปด้านหน้า
            currentMoveSpeed = speed + fastFallBoost;

            // ดึงลง
            rb.linearVelocity = new Vector3(
                currentMoveSpeed,
                -fastFallSpeed,
                rb.linearVelocity.z
            );
        }

        //if (minigamecam.activeSelf || minigamecam2.activeSelf)
        //{
        //miniGame1 = true;
        //rb.linearVelocity = Vector3.zero; // หยุดการเคลื่อนที่ทันที
        //}
        //else if (!isGroundedright && !isGroundedright2) // ถ้าไม่ติดผนังขวาให้วิ่งปกติ
        //{
        //rb.linearVelocity = new Vector3(speed, rb.linearVelocity.y, 0); // วิ่งอัตโนมัติเมื่อไม่อยู่ในมินิเกม
        //}
        //else if (checkSelfActive.activeSelf) // ถ้าอยู่ในมินิเกมให้หยุดการเคลื่อนที่
        //{
        //Timer += Time.deltaTime;

        //if (Timer >= DelayTime)
        //{
        //miniGame1 = false;
        //}
        //}
        //else
        //{
        //Timer = 0f;
        //}
        UpdateRunningState();


    }

    private void UpdateRunningState()
    {
        switch (runState)
        {
            case RunState.Running:UpdateNormalRunning();
                break;

            case RunState.Braking:UpdateBraking();
                break;

            case RunState.Stopped:
                // หยุดเฉพาะการวิ่งแกน X แต่ยังปล่อยให้แกน Y ตกตาม Gravity
                rb.linearVelocity = new Vector3(0f, rb.linearVelocity.y, 0f);
                break;

            case RunState.Accelerating:UpdateAccelerating();
                break;
        }
    }
    private void UpdateNormalRunning()
    {/*
        if (isGroundedright || isGroundedright2)
        {
            rb.linearVelocity = new Vector3(
                speedwallcheck,
                rb.linearVelocity.y,
                0f
            );

            return;
        }*/

        // ค่อย ๆ กลับจาก Boost ไปหาความเร็วพื้นฐานปัจจุบัน
        currentMoveSpeed = Mathf.MoveTowards(
            currentMoveSpeed,
            speed,
            boostRecoverySpeed * Time.deltaTime
        );

        rb.linearVelocity = new Vector3(
            currentMoveSpeed,
            rb.linearVelocity.y,
            0f
        );
    }

    private void UpdateBraking()
    {

        if (currentStopPoint == null)
        {
            StopAndOpenMinigame();
            return;
        }

        float distanceToStop =
            currentStopPoint.position.x - transform.position.x;

        // ถึงหรือเลย StopPoint แล้ว
        if (distanceToStop <= stopDistance)
        {
            StopAndOpenMinigame();
            return;
        }

        float newSpeed = Mathf.MoveTowards( rb.linearVelocity.x, 0f, currentBrakeDeceleration * Time.deltaTime);

        /*
         * ป้องกันความเร็วกลายเป็น 0 ก่อนถึง StopPoint
         * เพราะถ้าหยุดก่อนถึง จุดหยุด Player จะไปต่อไม่ได้
         */
        float minimumSpeed = 0.5f;

        if (distanceToStop > stopDistance)
        {
            newSpeed = Mathf.Max(newSpeed, minimumSpeed);
        }

        rb.linearVelocity = new Vector3(
            newSpeed,
            rb.linearVelocity.y,
            0f
        );
    }

    private void UpdateAccelerating()
    {

        float newSpeed = Mathf.MoveTowards(
            rb.linearVelocity.x,
            speed,
            accelerationSpeed * Time.deltaTime
        );

        rb.linearVelocity = new Vector3(
            newSpeed,
            rb.linearVelocity.y,
            0f
        );

        if (Mathf.Approximately(newSpeed, speed))
        {
            runState = RunState.Running;
            miniGame1 = false;
            canSlice = true;
            canJump = true;
            Animation.cantSlice = false;
            Pause.enabled = true;
        }
    }

    public void StartBraking(
    Transform stopPoint,
    GameObject minigameCameraObject)
    {
        if (runState == RunState.Braking ||
            runState == RunState.Stopped)
        {
            return;
        }

        currentStopPoint = stopPoint;
        targetMinigameCamera = minigameCameraObject;

        // ระยะจาก Player ไปถึง StopPoint
        float distanceToStop =
            currentStopPoint.position.x - transform.position.x;

        // ความเร็วจริงตอนเริ่มเบรก
        float currentSpeed =
            Mathf.Abs(rb.linearVelocity.x);

        if (distanceToStop > 0.01f)
        {
            // คำนวณแรงเบรกให้พอดีกับระยะที่เหลือ
            currentBrakeDeceleration =
                (currentSpeed * currentSpeed) /
                (2f * distanceToStop);
        }
        else
        {
            currentBrakeDeceleration = brakeSpeed;
        }

        // ป้องกันค่าต่ำหรือสูงเกินไป
        currentBrakeDeceleration =
            Mathf.Clamp(currentBrakeDeceleration, 1f, -3f);

        runState = RunState.Braking;

        Debug.Log(
            $"เริ่มเบรก | Speed = {currentSpeed:F2} " +
            $"Distance = {distanceToStop:F2} " +
            $"Brake = {currentBrakeDeceleration:F2}"
        );
    }

    private void StopAndOpenMinigame()
    {
        runState = RunState.Stopped;
        miniGame1 = true;

        rb.linearVelocity = new Vector3(0f, rb.linearVelocity.y, 0f);

        /*
         * จัดตำแหน่ง X ให้ตรงกับ StopPoint พอดี
         * แต่รักษา Y และ Z เดิมไว้
         */
        if (currentStopPoint != null)
        {
            Vector3 stopPosition = transform.position;
            stopPosition.x = currentStopPoint.position.x;

            rb.position = stopPosition;
        }

        //checkSelfActive.SetActive(false);

        if (targetMinigameCamera != null)
        {
            targetMinigameCamera.SetActive(true);
        }
    }

    public void FinishMinigame()
    {

        if (MiniGameSelector.Instance != null)
        {
            MiniGameSelector.Instance.CloseCurrentMiniGame();
        }

        currentStopPoint = null;
        targetMinigameCamera = null;

        rb.linearVelocity = new Vector3(
            0f,
            rb.linearVelocity.y,
            0f
        );

        runState = RunState.Accelerating;
    }

    //void OnTriggerEnter(Collider other)
    //{
    //    if (other.CompareTag("warp"))
    //    {
    //        checkSelfActive.SetActive(false);
    //        //maincam.enabled = false;
    //        minigamecam.SetActive(true);
    //    }

    //    if (other.CompareTag("warp2"))
    //    {
    //        checkSelfActive.SetActive(false);
    //        //maincam.enabled = false;
    //        minigamecam2.SetActive(true);
    //    }

    //}

}
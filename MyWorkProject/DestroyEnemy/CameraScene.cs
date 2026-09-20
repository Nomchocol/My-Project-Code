using UnityEngine;
using UnityEngine.SocialPlatforms;
using TMPro;

public class CameraScene : MonoBehaviour
{

    public static CameraScene instance;

    public float rotationSpeed = 1.0f; // ความเร็วในการหมุน
    private Quaternion startRotation; // การหมุนเริ่มต้น (มองฟ้า)
    private Quaternion targetRotation; // การหมุนเป้าหมาย (ตำแหน่งเดิม)
    public TMP_Text subText;
    private bool isRotatingdown = true;
    private bool isRotating = false; // สถานะการหมุน
    private bool hasMoved = false;
    private bool hasMoved2 = false;
    public bool startCutscene = false;
    private bool soundgun = true;
    private bool letgo = false;
    private AudioSource audioSource;  // ช่องเสียง
    public AudioClip clip;
    public GameObject MainCamera;
    public GameObject Camera1;
    public GameObject Camera2;
    public GameObject Camera3;
    public GameObject finalScene;
    public GameObject notshoot;

    void Awake()
    {
        instance = this;
    }

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        if (audioSource == null)
        {
            audioSource = GetComponent<AudioSource>();
        }
        // บันทึกการหมุนเป้าหมาย (ตำแหน่งเดิม)
        targetRotation = transform.rotation;

        // ตั้งค่าการหมุนเริ่มต้นให้กล้องมองฟ้า
        startRotation = Quaternion.Euler(70, transform.eulerAngles.y, transform.eulerAngles.z);
        transform.rotation = startRotation;
        MainCamera.SetActive(true);
        Camera1.SetActive(false);
        Camera2.SetActive(false);
        Camera3.SetActive(false);
        finalScene.SetActive(false);
        notshoot.SetActive(true);
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButtonDown(0) && soundgun)
        {
            GetComponent<CameraScene>().PlayOnce();
        }

        if (isRotatingdown)
        {
            subText.text = "ก็มาดิวะะ!!!";
            // ค่อย ๆ หมุนกล้องจาก startRotation ไป targetRotation
            transform.rotation = Quaternion.Lerp(transform.rotation, targetRotation, Time.deltaTime * rotationSpeed);

            if (Quaternion.Angle(transform.rotation, targetRotation) < 0.1f)
            {
                transform.rotation = targetRotation; // ตั้งค่าให้ตรงเป้าหมาย
                isRotatingdown = false; // หยุดการหมุน
            }
        }

        if (isRotating)
        {
            // ค่อย ๆ หมุนกล้องจาก startRotation ไป targetRotation
            transform.rotation = Quaternion.Lerp(transform.rotation, targetRotation, Time.deltaTime * 3);

            if (Quaternion.Angle(transform.rotation, targetRotation) < 0.1f)
            {
                transform.rotation = targetRotation; // ตั้งค่าให้ตรงเป้าหมาย
                isRotating = false; // หยุดการหมุน
            }
        }

        if (GameManager.instance.score >= 19 && !hasMoved2)
        {
            subText.text = "";
            Invoke(nameof(Scene1), 0.5f);


        }
        else if (!hasMoved)
        {
            // เรียกฟังก์ชัน GameOver() หลังจาก 4 วินาที หาก score ไม่ถึง 4
            Invoke(nameof(GameOver1), 6f);
        }

        if (GameManager.instance.score == 30 && hasMoved)
        {
            Invoke(nameof(cutsceneCamera1), 1f);
        }
        else if (hasMoved)
        {
            // เรียกฟังก์ชัน GameOver() หลังจาก 5 วินาที หาก score ไม่ถึง 4
            Invoke(nameof(GameOver3), 8f);
        }

        if (GameManager.instance.score == 37 && startCutscene)
        {
            Invoke(nameof(sceneEnd), 1f);
            hasMoved = true;
        }
        else if (startCutscene)
        {
            // เรียกฟังก์ชัน GameOver() หลังจาก 4 วินาที หาก score ไม่ถึง 4
            Invoke(nameof(GameOver4), 4.5f);
        }
    }

    public void PlayOnce()
    {
        if (clip != null)
        {
            audioSource.PlayOneShot(clip); // เล่นครั้งเดียว
        }
    }

    void GameOver(int Score)
    {
        if (GameManager.instance.score < Score)
        {
            GameManager.instance.GameOver();
        }
    }

    void GameOver1() => GameOver(19);
    void GameOver2() => GameOver(24);
    void GameOver3() => GameOver(30);
    void GameOver4() => GameOver(37);


    void Scene1()
    {
        targetRotation = Quaternion.Euler(0, 0, 0); // หมุนไปยังเป้าหมาย 
        isRotating = true;

        if (Quaternion.Angle(transform.rotation, Quaternion.Euler(0, 0, 0)) < 0.1f)
        {
            letgo = true;
            transform.position = Vector3.MoveTowards(transform.position, new Vector3(transform.position.x, transform.position.y, 30), Time.deltaTime * 6);
            if (GameManager.instance.score == 24)
            {
                if (Mathf.Approximately(transform.position.z, 30))
                {
                    Invoke(nameof(Scene2), 0.5f);
                }
            }
            else if (GameManager.instance.score <= 23 && letgo)
            {
                // เรียกฟังก์ชัน GameOver() หลังจาก 4 วินาที หาก score ไม่ถึง 4
                Invoke(nameof(GameOver2), 3f);
            }
        }

    }

    void Scene2()
    {
        targetRotation = Quaternion.Euler(0, 90, 0);
        notshoot.SetActive(false);
        isRotating = true;
        hasMoved2 = true;
        hasMoved = true;
        letgo = false;
    }

    void Scene3()
    {
        if (finalScene.activeSelf && !hasMoved)
        {
            targetRotation = Quaternion.Euler(0, 0, 0);
            isRotating = true;
        }
    }

    void sceneEnd()
    {
        soundgun = false;
        targetRotation = Quaternion.Euler(0, -35, 0);
        isRotating = true;
        startCutscene = false;
        Invoke(nameof(nextScene), 2f);
    }

    void nextScene()
    {
        GameManager.instance.nextscene2();
    }

    void cutsceneCamera1()
    {
        startCutscene = true;
        hasMoved = false;
        MainCamera.SetActive(false);
        Camera1.SetActive(true);
        Camera2.SetActive(false);
        Camera3.SetActive(false);
        Invoke(nameof(cutsceneCamera2), 3f);
    }

    void cutsceneCamera2()
    {
        MainCamera.SetActive(false);
        Camera1.SetActive(false);
        Camera2.SetActive(true);
        Camera3.SetActive(false);
        Invoke(nameof(cutsceneCamera3), 2f);
    }
    void cutsceneCamera3()
    {
        MainCamera.SetActive(false);
        Camera1.SetActive(false);
        Camera2.SetActive(false);
        Camera3.SetActive(true);
        Invoke(nameof(Gameplay), 2f);
    }
    void Gameplay()
    {
        finalScene.SetActive(true);
        MainCamera.SetActive(true);
        Camera1.SetActive(false);
        Camera2.SetActive(false);
        Camera3.SetActive(false);
        Invoke(nameof(Scene3), 1f);
    }


}

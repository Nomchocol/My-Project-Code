using System.Collections;
using UnityEngine;
using TMPro;

public class PlayerFly : MonoBehaviour
{
    [SerializeField] private TMP_Text flyTimeText;
    public float flyPower = 10f;
    public float flySpeed = 5f; 
    public float flyDuration = 5f;
    private bool isFlying = false;
    private bool canFly = false;
    private float flyTimeCounter;
    private Rigidbody2D rb;
    private Animator anim;
    private float remainingFlyTime = 0f;
    public float doubleTapTime = 0.5f;
    private float lastTapTime = 0;

    void Start()
    {
        anim = GetComponent<Animator>();
        rb = GetComponent<Rigidbody2D>();
        flyTimeText.text = "";
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.W) && canFly && !isFlying)
        {
            if (Time.time - lastTapTime < doubleTapTime)
            {
                StartCoroutine(FlyMode());
                remainingFlyTime = flyDuration;
                flyTimeText.text = remainingFlyTime.ToString("F1");

            }
            lastTapTime = Time.time;

        }

        if (isFlying)
        {
            remainingFlyTime -= Time.deltaTime;
            flyTimeText.text = remainingFlyTime.ToString("F1");
            anim.SetBool("fly", true);
        }
        else
        {
            flyTimeText.text = "";
            anim.SetBool("fly", false);
        }

        if (isFlying)
        {
            flyTimeCounter -= Time.deltaTime;
            if (flyTimeCounter <= 0)
            {
                StopFlying();
                anim.SetTrigger("jump");
            }
        }
    }

    public void EnableFly()
    {
        canFly = true; 
    }

    private IEnumerator FlyMode()
    {
        isFlying = true;
        anim.SetBool("fly", true);
        canFly = false; 
        rb.gravityScale = 0; 

        flyTimeCounter = flyDuration;
        float timer = 0;

        while (timer < flyDuration)
        {
            Vector2 moveDirection = Vector2.zero;

            if (Input.GetKey(KeyCode.W) || Input.GetKey(KeyCode.UpArrow)) moveDirection += Vector2.up;
            if (Input.GetKey(KeyCode.S) || Input.GetKey(KeyCode.DownArrow)) moveDirection += Vector2.down;
            if (Input.GetKey(KeyCode.A) || Input.GetKey(KeyCode.LeftArrow)) moveDirection += Vector2.left;
            if (Input.GetKey(KeyCode.D) || Input.GetKey(KeyCode.RightArrow)) moveDirection += Vector2.right;

            rb.linearVelocity = moveDirection.normalized * flySpeed; 

            timer += Time.deltaTime;
            yield return null;
        }

        StopFlying(); 
    }

    private void StopFlying()
    {
        isFlying = false;
        rb.gravityScale = 1.5f; 
        rb.linearVelocity = Vector2.zero; 
        anim.SetBool("fly", false); 
    }
}

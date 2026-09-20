using UnityEngine;

public class CheckAnimation : MonoBehaviour
{
    public PlayerController Checkjump;

    Animator anim;

    private bool slideCancelled = false;

    public bool cantSlice = false;

    void Start()
    {
        anim = GetComponent<Animator>();
    }

    void Update()
    {
        // -------------------------
        // Jump Animation
        // -------------------------

        anim.SetBool("isJump", !Checkjump.isGrounded);


        // -------------------------
        // Slide Input
        // -------------------------

        bool slideHeld =
            Input.GetKey(KeyCode.DownArrow) ||
            Input.GetKey(KeyCode.S) && !cantSlice;

        bool slideReleased =
            Input.GetKeyUp(KeyCode.DownArrow) ||
            Input.GetKeyUp(KeyCode.S) && !cantSlice;


        // ปล่อยปุ่ม Slide แล้ว สามารถ Slide ใหม่ได้
        if (slideReleased)
        {
            slideCancelled = false;
        }


        // -------------------------
        // กด Space ตอนกำลัง Slide
        // -------------------------

        if (Input.GetKeyDown(KeyCode.Space) && slideHeld)
        {
            slideCancelled = true;

            anim.SetBool("Sliding", false);
        }


        // -------------------------
        // Slide Animation
        // -------------------------

        if (slideHeld && !slideCancelled)
        {
            anim.SetBool("Sliding", true);
        }
        else
        {
            anim.SetBool("Sliding", false);
        }
    }
}
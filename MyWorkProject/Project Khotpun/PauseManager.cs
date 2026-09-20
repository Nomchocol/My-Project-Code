using System.Collections;
using System.Xml.Serialization;
using UnityEngine;
using UnityEngine.InputSystem.XR;
using UnityEngine.SceneManagement;

public class PauseManager : MonoBehaviour
{
    public PlayerController controller;
    public CheckAnimation Slice;

    public GameObject pauseUI;

    [Header("Pause Animators")]
    public Animator[] pauseAnimators;

    [Header("Timing")]
    public float pressedDelay = 0.1f;
    public float closeAnimationTime = 0.4f;

    public bool isPaused = false;
    private bool isClosing = false;

    public GameObject tblackEnd;

    private void Start()
    {
        tblackEnd.SetActive(false);
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            if (isClosing)
                return;

            if (isPaused)
                Resume();
            else
                Pause();
        }
    }

    public void Pause()
    {
        pauseUI.SetActive(true);

        controller.canJump = false;
        controller.canSlice = false;
        Slice.cantSlice = true;
        Time.timeScale = 0f;
        isPaused = true;
    }

    public void Resume()
    {
        if (!isPaused || isClosing)
            return;

        controller.canJump = true;
        controller.canSlice = true;
        Slice.cantSlice = false;
        StartCoroutine(ResumeAnimation());
    }

    public void restart()
    {
        tblackEnd.SetActive(true);
        StartCoroutine(DelayreStart());
    }

    IEnumerator ResumeAnimation()
    {
        isClosing = true;

        // ให้ Resume Pressed animation เล่นก่อนนิดหนึ่ง
        yield return new WaitForSecondsRealtime(pressedDelay);

        // สั่ง UI ทุกตัวเล่น Animation ออกพร้อมกัน
        foreach (Animator anim in pauseAnimators)
        {
            if (anim != null)
            {
                anim.SetTrigger("Close");
            }
        }

        // รอ Animation ออกเล่นจนจบ
        yield return new WaitForSecondsRealtime(closeAnimationTime);

        pauseUI.SetActive(false);

        Time.timeScale = 1f;
        isPaused = false;
        isClosing = false;
    }

    IEnumerator DelayreStart()
    {
        yield return new WaitForSecondsRealtime(1f);

        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }
}
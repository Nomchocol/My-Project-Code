using UnityEngine;
using UnityEngine.InputSystem.XR;

public class MenuGame : MonoBehaviour
{

    public GameObject UIgameRun;

    public GameObject UI_MENU;

    public PauseManager Pause;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        Time.timeScale = 0f;
        UIgameRun.SetActive(false);
        UI_MENU.SetActive(true);
        Pause.enabled = false;
    }

    // Update is called once per frame
    public void StartTheGame()
    {
        Time.timeScale = 1f;
        UIgameRun.SetActive(true);
        UI_MENU.SetActive(false);
        Pause.enabled = true;
    }
}

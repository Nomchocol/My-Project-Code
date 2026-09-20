using UnityEngine;
using UnityEngine.SceneManagement;

public class MenuScene : MonoBehaviour
{

    public void StartGame()
    {
        Time.timeScale = 1f; 
        SceneManager.LoadScene("SampleScene"); 
    }

    public void QuitGame()
    {
        Application.Quit(); 
    }

    public void MainMenu()
    {
        Time.timeScale = 1f;
        SceneManager.LoadScene("MenuScene");
    }
}

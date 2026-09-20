using UnityEngine;
using UnityEngine.SceneManagement;

public class PlayerDeath : MonoBehaviour
{
    public GameObject deathMenuUI; // อ้างอิงถึง AudioSource ที่จะเล่นเสียง

    private bool isDead = false;

    private void Start()
    {
        deathMenuUI.SetActive(false);
    }

    public void Die()
    {
        if (!isDead)
        {
            isDead = true;
            deathMenuUI.SetActive(true); 
            Time.timeScale = 0f; 
        }
    }



    public void Retry()
    {
        Time.timeScale = 1f; 
        SceneManager.LoadScene(SceneManager.GetActiveScene().name); 
    }

    public void MainMenu()
    {
        Time.timeScale = 1f; 
        SceneManager.LoadScene("MenuScene");
    }

    public void QuitGame()
    {
        Application.Quit(); 
    }
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Return)) 
        {
            Die();
        }
    }

}

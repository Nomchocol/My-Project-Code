using UnityEngine;

public class MiniGameSelector : MonoBehaviour
{
    public static MiniGameSelector Instance;

    [Header("Mini Games In Scene")]
    [SerializeField] private GameObject[] miniGames;

    private GameObject currentMiniGame;

    private void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }

        Instance = this;

        CloseAllMiniGames();
    }

    public GameObject GetRandomMiniGame()
    {
        if (miniGames == null || miniGames.Length == 0)
        {
            Debug.LogError("ยังไม่ได้ใส่มินิเกมใน MiniGameSelector");
            return null;
        }

        int randomIndex = Random.Range(0, miniGames.Length);

        currentMiniGame = miniGames[randomIndex];

        if (currentMiniGame == null)
        {
            Debug.LogError($"Mini Games ช่อง {randomIndex} เป็น None");
            return null;
        }

        Debug.Log($"สุ่มได้มินิเกม: {currentMiniGame.name}");

        return currentMiniGame;
    }

    public void CloseCurrentMiniGame()
    {
        if (currentMiniGame != null)
        {
            currentMiniGame.SetActive(false);
            currentMiniGame = null;
        }
    }

    private void CloseAllMiniGames()
    {
        if (miniGames == null)
            return;

        foreach (GameObject miniGame in miniGames)
        {
            if (miniGame != null)
            {
                miniGame.SetActive(false);
            }
        }
    }
}
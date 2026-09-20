using UnityEngine;
using UnityEngine.SceneManagement;
using TMPro;

public class nextscene : MonoBehaviour
{
    public GameObject panel;
    public TMP_Text subText;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        panel.SetActive(false);
    }

    // Update is called once per frame
    void Update()
    {
        if (Cameracutscene.instance.startnextscene == true)
        {
            transform.position = Vector3.MoveTowards(transform.position, new Vector3(6.88f, 0.8999996f, 9.17f), Time.deltaTime * 20f);
        }
    }

    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            panel.SetActive(true);
            Invoke(nameof(nextlevel), 1.5f);
        }
    }

    void nextlevel()
    {
        Invoke(nameof(nextlevelfalse), 2f);
        subText.text = "เวรรร....";
    }

    void nextlevelfalse()
    {
        Invoke(nameof(nextleveltrue), 2.3f);
        subText.text = "จะเอาอย่างงี้ใช่ไหมม..ได้้เลยย";
    }

    void nextleveltrue()
    {
        SceneManager.LoadScene("SampleScene");
    }
}

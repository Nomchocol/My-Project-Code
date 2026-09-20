using UnityEngine;

public class EnemySpawn3 : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Cameracutscene.instance.spawnnew == true)
        {
            transform.position = Vector3.MoveTowards(transform.position, new Vector3(16.8320007f, 1.89899995f, 11.8178329f), Time.deltaTime * 10f);
        }
    }
}

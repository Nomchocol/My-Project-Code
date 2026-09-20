using UnityEngine;

public class EnemySpawn2 : MonoBehaviour
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
            transform.position = Vector3.MoveTowards(transform.position, new Vector3(17.4880009f, 3.43899989f, 12.6149998f), Time.deltaTime * 10f);
        }
    }
}

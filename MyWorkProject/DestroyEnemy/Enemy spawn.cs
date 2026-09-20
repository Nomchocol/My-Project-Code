using UnityEngine;

public class Enemyspawn : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Cameracutscene.instance.stop == true)
        {
            transform.position = Vector3.MoveTowards(transform.position, new Vector3(transform.position.x, transform.position.y, 2.749f), Time.deltaTime * 10f);
        }
    }
}

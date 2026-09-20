using UnityEngine;

public class Traps2 : MonoBehaviour
{
    public Animator Trap;

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.CompareTag("Player"))
        {
            Trap.SetInteger("Move", 2);
        }
    }

}

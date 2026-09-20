using UnityEngine;

public class blockjumpslice : MonoBehaviour
{
    public CheckAnimation Slice;

    public PauseManager Pause;

    public PlayerController controller;
    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            controller.canJump = false;
            controller.canSlice = false;
            Slice.cantSlice = true;
            Pause.enabled = false;
        }
    }
}

using System.Collections;
using UnityEngine;

public class GroundTile : MonoBehaviour
{
    [Header("Pattern")]
    public Transform patternRoot;

    [Header("Recycle Settings")]
    public float recycleDelay = 2f;

    private GameObject currentPattern;
    protected bool used;

    public void Recycle()
    {
        if (used)
            return;

        used = true;

        StartCoroutine(RecycleAfterDelay());
    }

    private IEnumerator RecycleAfterDelay()
    {
        yield return new WaitForSeconds(recycleDelay);

        if (GroundManager.Instance == null)
        {
            Debug.LogError("ไม่พบ GroundManager.Instance");
            used = false;
            yield break;
        }

        GroundManager.Instance.RecycleTile(this);
    }

    public void SetCurrentPattern(GameObject pattern)
    {
        currentPattern = pattern;
    }

    public void ClearPattern()
    {
        if (currentPattern != null)
        {
            Destroy(currentPattern);
            currentPattern = null;
        }
    }

    public virtual void ResetTile()
    {
        used = false;
    }
}
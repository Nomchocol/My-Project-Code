using System.Collections.Generic;
using UnityEngine;

public class GroundManager : MonoBehaviour
{
    public static GroundManager Instance;

    [Header("Ground Settings")]
    public List<GroundTile> activeTiles = new List<GroundTile>();
    public float tileLength = 30f;

    [Header("Pattern Prefabs")]
    public GameObject[] patterns;

    private void Awake()
    {
        Instance = this;
    }

    private void Start()
    {
        foreach (GroundTile tile in activeTiles)
        {
            // ไม่สุ่ม Pattern ให้ MiniGameTile
            if (tile is not MiniGameTile)
            {
                SetRandomPattern(tile);
            }
        }
    }

    public void RecycleTile(GroundTile tile)
    {
        if (activeTiles == null || activeTiles.Count == 0)
        {
            Debug.LogError("ไม่มี Tile ใน activeTiles");
            return;
        }

        GroundTile lastTile = activeTiles[activeTiles.Count - 1];

        tile.transform.position =
            lastTile.transform.position +
            Vector3.right * tileLength;

        activeTiles.Remove(tile);
        activeTiles.Add(tile);

        // Tile ปกติสุ่ม Pattern แต่ MiniGameTile ไม่ต้องสุ่ม
        if (tile is not MiniGameTile)
        {
            SetRandomPattern(tile);
        }

        tile.ResetTile();
    }

    private void SetRandomPattern(GroundTile tile)
    {
        tile.ClearPattern();

        if (tile.patternRoot == null)
        {
            Debug.LogWarning(
                $"{tile.name} ไม่มี PatternRoot",
                tile.gameObject
            );
            return;
        }

        if (patterns == null || patterns.Length == 0)
        {
            Debug.LogWarning("ยังไม่ได้ใส่ Pattern ใน GroundManager");
            return;
        }

        int randomIndex = Random.Range(0, patterns.Length);

        GameObject newPattern = Instantiate(
            patterns[randomIndex],
            tile.patternRoot.position,
            tile.patternRoot.rotation,
            tile.patternRoot
        );

        tile.SetCurrentPattern(newPattern);
    }
}
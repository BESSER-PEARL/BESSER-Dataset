





import java.util.List;
import java.util.ArrayList;

public class Item1  {

    private float itemCost;
    private String itemCount;
    private String itemName;
    private int itemCode;



    public Item1(
        float itemCost,        String itemCount,        String itemName,        int itemCode    ) {
        this.itemCost = itemCost;
        this.itemCount = itemCount;
        this.itemName = itemName;
        this.itemCode = itemCode;
    }


    public float getItemcost() {
        return itemCost;
    }

    public void setItemcost(float itemCost) {
        this.itemCost = itemCost;
    }
    public String getItemcount() {
        return itemCount;
    }

    public void setItemcount(String itemCount) {
        this.itemCount = itemCount;
    }
    public String getItemname() {
        return itemName;
    }

    public void setItemname(String itemName) {
        this.itemName = itemName;
    }
    public int getItemcode() {
        return itemCode;
    }

    public void setItemcode(int itemCode) {
        this.itemCode = itemCode;
    }


}
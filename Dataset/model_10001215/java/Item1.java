





import java.util.List;
import java.util.ArrayList;

public class Item1  {

    private float itemCost;
    private int itemCode;
    private String itemName;
    private String itemCount;



    public Item1(
        float itemCost,        int itemCode,        String itemName,        String itemCount    ) {
        this.itemCost = itemCost;
        this.itemCode = itemCode;
        this.itemName = itemName;
        this.itemCount = itemCount;
    }


    public float getItemcost() {
        return itemCost;
    }

    public void setItemcost(float itemCost) {
        this.itemCost = itemCost;
    }
    public int getItemcode() {
        return itemCode;
    }

    public void setItemcode(int itemCode) {
        this.itemCode = itemCode;
    }
    public String getItemname() {
        return itemName;
    }

    public void setItemname(String itemName) {
        this.itemName = itemName;
    }
    public String getItemcount() {
        return itemCount;
    }

    public void setItemcount(String itemCount) {
        this.itemCount = itemCount;
    }


}
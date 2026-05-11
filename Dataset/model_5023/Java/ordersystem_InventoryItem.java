





import java.util.List;
import java.util.ArrayList;

public class ordersystem_InventoryItem  {

    private String nextStockDate;
    private int inStock;
    private int restockThreshold;



    public ordersystem_InventoryItem(
        String nextStockDate,        int inStock,        int restockThreshold    ) {
        this.nextStockDate = nextStockDate;
        this.inStock = inStock;
        this.restockThreshold = restockThreshold;
    }


    public String getNextstockdate() {
        return nextStockDate;
    }

    public void setNextstockdate(String nextStockDate) {
        this.nextStockDate = nextStockDate;
    }
    public int getInstock() {
        return inStock;
    }

    public void setInstock(int inStock) {
        this.inStock = inStock;
    }
    public int getRestockthreshold() {
        return restockThreshold;
    }

    public void setRestockthreshold(int restockThreshold) {
        this.restockThreshold = restockThreshold;
    }


}






import java.util.List;
import java.util.ArrayList;

public class Items  {

    private int itemid;





    private OnlineShopping onlineshopping;


    public Items(
        int itemid    ) {
        this.itemid = itemid;
    }


    public int getItemid() {
        return itemid;
    }

    public void setItemid(int itemid) {
        this.itemid = itemid;
    }

    public OnlineShopping getOnlineshopping() {
        return onlineshopping;
    }

    public void setOnlineshopping(OnlineShopping onlineshopping) {
        this.onlineshopping = onlineshopping;
    }

}
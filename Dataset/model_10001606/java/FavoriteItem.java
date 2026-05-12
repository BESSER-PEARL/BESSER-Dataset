





import java.util.List;
import java.util.ArrayList;

public class FavoriteItem  {

    private String UserId;
    private String ItemId;





    private Item item;


    public FavoriteItem(
        String UserId,        String ItemId    ) {
        this.UserId = UserId;
        this.ItemId = ItemId;
    }


    public String getUserid() {
        return UserId;
    }

    public void setUserid(String UserId) {
        this.UserId = UserId;
    }
    public String getItemid() {
        return ItemId;
    }

    public void setItemid(String ItemId) {
        this.ItemId = ItemId;
    }

    public Item getItem() {
        return item;
    }

    public void setItem(Item item) {
        this.item = item;
    }

}
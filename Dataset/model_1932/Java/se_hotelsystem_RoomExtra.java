





import java.util.List;
import java.util.ArrayList;

public class se_hotelsystem_RoomExtra  {

    private String description;
    private float price;



    public se_hotelsystem_RoomExtra(
        String description,        float price    ) {
        this.description = description;
        this.price = price;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }


}
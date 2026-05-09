





import java.util.List;
import java.util.ArrayList;

public class newClasses_RoomType  {

    private String price;
    private String type;



    public newClasses_RoomType(
        String price,        String type    ) {
        this.price = price;
        this.type = type;
    }


    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}
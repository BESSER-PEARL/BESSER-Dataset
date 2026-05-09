





import java.util.List;
import java.util.ArrayList;

public class se_roomManager_RoomType extends IRoomType {

    private String name;
    private float price;
    private String description;
    private int numberOfBeds;



    public se_roomManager_RoomType(
        String name,        float price,        String description,        int numberOfBeds    ) {
        super(
        );
        this.name = name;
        this.price = price;
        this.description = description;
        this.numberOfBeds = numberOfBeds;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getNumberofbeds() {
        return numberOfBeds;
    }

    public void setNumberofbeds(int numberOfBeds) {
        this.numberOfBeds = numberOfBeds;
    }


}
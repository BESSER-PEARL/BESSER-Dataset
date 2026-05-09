





import java.util.List;
import java.util.ArrayList;

public class se_hotelsystem_RoomType  {

    private int numBeds;
    private float pricePerNight;
    private String description;
    private String name;



    public se_hotelsystem_RoomType(
        int numBeds,        float pricePerNight,        String description,        String name    ) {
        this.numBeds = numBeds;
        this.pricePerNight = pricePerNight;
        this.description = description;
        this.name = name;
    }


    public int getNumbeds() {
        return numBeds;
    }

    public void setNumbeds(int numBeds) {
        this.numBeds = numBeds;
    }
    public float getPricepernight() {
        return pricePerNight;
    }

    public void setPricepernight(float pricePerNight) {
        this.pricePerNight = pricePerNight;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
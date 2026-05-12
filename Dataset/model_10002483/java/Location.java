





import java.util.List;
import java.util.ArrayList;

public class Location  {

    private String attribute;
    private int loc_id;
    private String loc_name;





    private Hotels hotels;


    public Location(
        String attribute,        int loc_id,        String loc_name    ) {
        this.attribute = attribute;
        this.loc_id = loc_id;
        this.loc_name = loc_name;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getLoc_id() {
        return loc_id;
    }

    public void setLoc_id(int loc_id) {
        this.loc_id = loc_id;
    }
    public String getLoc_name() {
        return loc_name;
    }

    public void setLoc_name(String loc_name) {
        this.loc_name = loc_name;
    }

    public Hotels getHotels() {
        return hotels;
    }

    public void setHotels(Hotels hotels) {
        this.hotels = hotels;
    }

}
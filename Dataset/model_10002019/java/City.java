





import java.util.List;
import java.util.ArrayList;

public class City  {

    private String city;
    private int id;





    private Hotels hotels;


    public City(
        String city,        int id    ) {
        this.city = city;
        this.id = id;
    }


    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Hotels getHotels() {
        return hotels;
    }

    public void setHotels(Hotels hotels) {
        this.hotels = hotels;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Rooms  {

    private String name;
    private String room_description;
    private int price;
    private int id;





    private Hotels hotels;


    public Rooms(
        String name,        String room_description,        int price,        int id    ) {
        this.name = name;
        this.room_description = room_description;
        this.price = price;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRoom_description() {
        return room_description;
    }

    public void setRoom_description(String room_description) {
        this.room_description = room_description;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
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






import java.util.List;
import java.util.ArrayList;

public class Rooms  {

    private int id;
    private int checkout_date;
    private int price;
    private String room_description;
    private int checkin_date;
    private String name;





    private Hotels hotels;


    public Rooms(
        int id,        int checkout_date,        int price,        String room_description,        int checkin_date,        String name    ) {
        this.id = id;
        this.checkout_date = checkout_date;
        this.price = price;
        this.room_description = room_description;
        this.checkin_date = checkin_date;
        this.name = name;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getCheckout_date() {
        return checkout_date;
    }

    public void setCheckout_date(int checkout_date) {
        this.checkout_date = checkout_date;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getRoom_description() {
        return room_description;
    }

    public void setRoom_description(String room_description) {
        this.room_description = room_description;
    }
    public int getCheckin_date() {
        return checkin_date;
    }

    public void setCheckin_date(int checkin_date) {
        this.checkin_date = checkin_date;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Hotels getHotels() {
        return hotels;
    }

    public void setHotels(Hotels hotels) {
        this.hotels = hotels;
    }

}
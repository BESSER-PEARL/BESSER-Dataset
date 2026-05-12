





import java.util.List;
import java.util.ArrayList;

public class Guest  {

    private int id;
    private int Phone_no_;
    private String address;
    private String Nmae;





    private Hotels hotels;




    private Manager manager;




    private Rooms rooms;


    public Guest(
        int id,        int Phone_no_,        String address,        String Nmae    ) {
        this.id = id;
        this.Phone_no_ = Phone_no_;
        this.address = address;
        this.Nmae = Nmae;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getPhone_no_() {
        return Phone_no_;
    }

    public void setPhone_no_(int Phone_no_) {
        this.Phone_no_ = Phone_no_;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getNmae() {
        return Nmae;
    }

    public void setNmae(String Nmae) {
        this.Nmae = Nmae;
    }

    public Hotels getHotels() {
        return hotels;
    }

    public void setHotels(Hotels hotels) {
        this.hotels = hotels;
    }
    public Manager getManager() {
        return manager;
    }

    public void setManager(Manager manager) {
        this.manager = manager;
    }
    public Rooms getRooms() {
        return rooms;
    }

    public void setRooms(Rooms rooms) {
        this.rooms = rooms;
    }

}
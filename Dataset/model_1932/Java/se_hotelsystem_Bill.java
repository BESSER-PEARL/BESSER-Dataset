





import java.util.List;
import java.util.ArrayList;

public class se_hotelsystem_Bill  {

    private float price;
    private int billID;





    private hotelsystem_RoomReservation hotelsystem_roomreservation;


    public se_hotelsystem_Bill(
        float price,        int billID    ) {
        this.price = price;
        this.billID = billID;
    }


    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public int getBillid() {
        return billID;
    }

    public void setBillid(int billID) {
        this.billID = billID;
    }

    public hotelsystem_RoomReservation getHotelsystem_roomreservation() {
        return hotelsystem_roomreservation;
    }

    public void setHotelsystem_roomreservation(hotelsystem_RoomReservation hotelsystem_roomreservation) {
        this.hotelsystem_roomreservation = hotelsystem_roomreservation;
    }

}






import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Room extends Costable {

    private boolean underCleaning;
    private boolean underRepair;
    private int maxNbrPeople;
    private float size;
    private int roomNumber;
    private String type;
    private String internalComment;





    private HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking;


    public HotelManagementClassDiagram_Room(
        boolean underCleaning,        boolean underRepair,        int maxNbrPeople,        float size,        int roomNumber,        String type,        String internalComment    ) {
        super(
        );
        this.underCleaning = underCleaning;
        this.underRepair = underRepair;
        this.maxNbrPeople = maxNbrPeople;
        this.size = size;
        this.roomNumber = roomNumber;
        this.type = type;
        this.internalComment = internalComment;
    }


    public boolean getUndercleaning() {
        return underCleaning;
    }

    public void setUndercleaning(boolean underCleaning) {
        this.underCleaning = underCleaning;
    }
    public boolean getUnderrepair() {
        return underRepair;
    }

    public void setUnderrepair(boolean underRepair) {
        this.underRepair = underRepair;
    }
    public int getMaxnbrpeople() {
        return maxNbrPeople;
    }

    public void setMaxnbrpeople(int maxNbrPeople) {
        this.maxNbrPeople = maxNbrPeople;
    }
    public float getSize() {
        return size;
    }

    public void setSize(float size) {
        this.size = size;
    }
    public int getRoomnumber() {
        return roomNumber;
    }

    public void setRoomnumber(int roomNumber) {
        this.roomNumber = roomNumber;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getInternalcomment() {
        return internalComment;
    }

    public void setInternalcomment(String internalComment) {
        this.internalComment = internalComment;
    }

    public HotelManagementClassDiagram_Booking getHotelmanagementclassdiagram_booking() {
        return hotelmanagementclassdiagram_booking;
    }

    public void setHotelmanagementclassdiagram_booking(HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking) {
        this.hotelmanagementclassdiagram_booking = hotelmanagementclassdiagram_booking;
    }

}
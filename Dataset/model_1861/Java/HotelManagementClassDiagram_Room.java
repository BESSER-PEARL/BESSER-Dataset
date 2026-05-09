





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Room  {

    private boolean underRepair;
    private float size;
    private int roomNumber;
    private boolean booked;
    private String roomName;
    private String internalComment;
    private boolean underCleaning;
    private String types;
    private int maxNbrPeople;





    private HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking;


    public HotelManagementClassDiagram_Room(
        boolean underRepair,        float size,        int roomNumber,        boolean booked,        String roomName,        String internalComment,        boolean underCleaning,        String types,        int maxNbrPeople    ) {
        this.underRepair = underRepair;
        this.size = size;
        this.roomNumber = roomNumber;
        this.booked = booked;
        this.roomName = roomName;
        this.internalComment = internalComment;
        this.underCleaning = underCleaning;
        this.types = types;
        this.maxNbrPeople = maxNbrPeople;
    }


    public boolean getUnderrepair() {
        return underRepair;
    }

    public void setUnderrepair(boolean underRepair) {
        this.underRepair = underRepair;
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
    public boolean getBooked() {
        return booked;
    }

    public void setBooked(boolean booked) {
        this.booked = booked;
    }
    public String getRoomname() {
        return roomName;
    }

    public void setRoomname(String roomName) {
        this.roomName = roomName;
    }
    public String getInternalcomment() {
        return internalComment;
    }

    public void setInternalcomment(String internalComment) {
        this.internalComment = internalComment;
    }
    public boolean getUndercleaning() {
        return underCleaning;
    }

    public void setUndercleaning(boolean underCleaning) {
        this.underCleaning = underCleaning;
    }
    public String getTypes() {
        return types;
    }

    public void setTypes(String types) {
        this.types = types;
    }
    public int getMaxnbrpeople() {
        return maxNbrPeople;
    }

    public void setMaxnbrpeople(int maxNbrPeople) {
        this.maxNbrPeople = maxNbrPeople;
    }

    public HotelManagementClassDiagram_Booking getHotelmanagementclassdiagram_booking() {
        return hotelmanagementclassdiagram_booking;
    }

    public void setHotelmanagementclassdiagram_booking(HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking) {
        this.hotelmanagementclassdiagram_booking = hotelmanagementclassdiagram_booking;
    }

}
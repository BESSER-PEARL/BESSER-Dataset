





import java.util.List;
import java.util.ArrayList;

public class se_bookingSystem_FreeRoomTypesDTO  {

    private float pricePerNight;
    private String roomTypeDescription;
    private int numFreeRooms;
    private int numBeds;



    public se_bookingSystem_FreeRoomTypesDTO(
        float pricePerNight,        String roomTypeDescription,        int numFreeRooms,        int numBeds    ) {
        this.pricePerNight = pricePerNight;
        this.roomTypeDescription = roomTypeDescription;
        this.numFreeRooms = numFreeRooms;
        this.numBeds = numBeds;
    }


    public float getPricepernight() {
        return pricePerNight;
    }

    public void setPricepernight(float pricePerNight) {
        this.pricePerNight = pricePerNight;
    }
    public String getRoomtypedescription() {
        return roomTypeDescription;
    }

    public void setRoomtypedescription(String roomTypeDescription) {
        this.roomTypeDescription = roomTypeDescription;
    }
    public int getNumfreerooms() {
        return numFreeRooms;
    }

    public void setNumfreerooms(int numFreeRooms) {
        this.numFreeRooms = numFreeRooms;
    }
    public int getNumbeds() {
        return numBeds;
    }

    public void setNumbeds(int numBeds) {
        this.numBeds = numBeds;
    }


}
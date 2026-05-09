





import java.util.List;
import java.util.ArrayList;

public class se_hotelsystem_FreeRoomTypesDTO  {

    private String roomTypeDescription;
    private float pricePerNight;
    private int numFreeRooms;
    private int numBeds;



    public se_hotelsystem_FreeRoomTypesDTO(
        String roomTypeDescription,        float pricePerNight,        int numFreeRooms,        int numBeds    ) {
        this.roomTypeDescription = roomTypeDescription;
        this.pricePerNight = pricePerNight;
        this.numFreeRooms = numFreeRooms;
        this.numBeds = numBeds;
    }


    public String getRoomtypedescription() {
        return roomTypeDescription;
    }

    public void setRoomtypedescription(String roomTypeDescription) {
        this.roomTypeDescription = roomTypeDescription;
    }
    public float getPricepernight() {
        return pricePerNight;
    }

    public void setPricepernight(float pricePerNight) {
        this.pricePerNight = pricePerNight;
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
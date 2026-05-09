





import java.util.List;
import java.util.ArrayList;

public class tda593_facilities_Room  {

    private String description;
    private String roomNumber;
    private boolean isOperational;
    private boolean isBeingCleaned;
    private int floor;
    private String disabilityApprovals;
    private String photos;



    public tda593_facilities_Room(
        String description,        String roomNumber,        boolean isOperational,        boolean isBeingCleaned,        int floor,        String disabilityApprovals,        String photos    ) {
        this.description = description;
        this.roomNumber = roomNumber;
        this.isOperational = isOperational;
        this.isBeingCleaned = isBeingCleaned;
        this.floor = floor;
        this.disabilityApprovals = disabilityApprovals;
        this.photos = photos;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getRoomnumber() {
        return roomNumber;
    }

    public void setRoomnumber(String roomNumber) {
        this.roomNumber = roomNumber;
    }
    public boolean getIsoperational() {
        return isOperational;
    }

    public void setIsoperational(boolean isOperational) {
        this.isOperational = isOperational;
    }
    public boolean getIsbeingcleaned() {
        return isBeingCleaned;
    }

    public void setIsbeingcleaned(boolean isBeingCleaned) {
        this.isBeingCleaned = isBeingCleaned;
    }
    public int getFloor() {
        return floor;
    }

    public void setFloor(int floor) {
        this.floor = floor;
    }
    public String getDisabilityapprovals() {
        return disabilityApprovals;
    }

    public void setDisabilityapprovals(String disabilityApprovals) {
        this.disabilityApprovals = disabilityApprovals;
    }
    public String getPhotos() {
        return photos;
    }

    public void setPhotos(String photos) {
        this.photos = photos;
    }


}
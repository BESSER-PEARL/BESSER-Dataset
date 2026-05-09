





import java.util.List;
import java.util.ArrayList;

public class RootElement_Room  {

    private String name;
    private String needCleaning;
    private String isOccupied;





    private RootElement_RoomBooking rootelement_roombooking;


    public RootElement_Room(
        String name,        String needCleaning,        String isOccupied    ) {
        this.name = name;
        this.needCleaning = needCleaning;
        this.isOccupied = isOccupied;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNeedcleaning() {
        return needCleaning;
    }

    public void setNeedcleaning(String needCleaning) {
        this.needCleaning = needCleaning;
    }
    public String getIsoccupied() {
        return isOccupied;
    }

    public void setIsoccupied(String isOccupied) {
        this.isOccupied = isOccupied;
    }

    public RootElement_RoomBooking getRootelement_roombooking() {
        return rootelement_roombooking;
    }

    public void setRootelement_roombooking(RootElement_RoomBooking rootelement_roombooking) {
        this.rootelement_roombooking = rootelement_roombooking;
    }

}
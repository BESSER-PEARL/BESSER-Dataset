





import java.util.List;
import java.util.ArrayList;

public class tda593_facilities_ConferenceRoom extends Room {

    private String equipment;
    private int numberOfSeats;



    public tda593_facilities_ConferenceRoom(
        String equipment,        int numberOfSeats    ) {
        super(
        );
        this.equipment = equipment;
        this.numberOfSeats = numberOfSeats;
    }


    public String getEquipment() {
        return equipment;
    }

    public void setEquipment(String equipment) {
        this.equipment = equipment;
    }
    public int getNumberofseats() {
        return numberOfSeats;
    }

    public void setNumberofseats(int numberOfSeats) {
        this.numberOfSeats = numberOfSeats;
    }


}
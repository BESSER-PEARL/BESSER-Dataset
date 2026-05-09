





import java.util.List;
import java.util.ArrayList;

public class tda593_facilities_GuestRoom extends Room {

    private int numberOfBeds;
    private int numberOfExtrabeds;



    public tda593_facilities_GuestRoom(
        int numberOfBeds,        int numberOfExtrabeds    ) {
        super(
        );
        this.numberOfBeds = numberOfBeds;
        this.numberOfExtrabeds = numberOfExtrabeds;
    }


    public int getNumberofbeds() {
        return numberOfBeds;
    }

    public void setNumberofbeds(int numberOfBeds) {
        this.numberOfBeds = numberOfBeds;
    }
    public int getNumberofextrabeds() {
        return numberOfExtrabeds;
    }

    public void setNumberofextrabeds(int numberOfExtrabeds) {
        this.numberOfExtrabeds = numberOfExtrabeds;
    }


}
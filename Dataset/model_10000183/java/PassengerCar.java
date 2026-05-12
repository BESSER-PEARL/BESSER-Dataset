





import java.util.List;
import java.util.ArrayList;

public class PassengerCar  {

    private int numSeatsOccupied;
    private int NUMSEATS;



    public PassengerCar(
        int numSeatsOccupied,        int NUMSEATS    ) {
        this.numSeatsOccupied = numSeatsOccupied;
        this.NUMSEATS = NUMSEATS;
    }


    public int getNumseatsoccupied() {
        return numSeatsOccupied;
    }

    public void setNumseatsoccupied(int numSeatsOccupied) {
        this.numSeatsOccupied = numSeatsOccupied;
    }
    public int getNumseats() {
        return NUMSEATS;
    }

    public void setNumseats(int NUMSEATS) {
        this.NUMSEATS = NUMSEATS;
    }


}
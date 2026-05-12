





import java.util.List;
import java.util.ArrayList;

public class Coach  {

    private int seatsFilled;
    private int numberOfSeats;



    public Coach(
        int seatsFilled,        int numberOfSeats    ) {
        this.seatsFilled = seatsFilled;
        this.numberOfSeats = numberOfSeats;
    }


    public int getSeatsfilled() {
        return seatsFilled;
    }

    public void setSeatsfilled(int seatsFilled) {
        this.seatsFilled = seatsFilled;
    }
    public int getNumberofseats() {
        return numberOfSeats;
    }

    public void setNumberofseats(int numberOfSeats) {
        this.numberOfSeats = numberOfSeats;
    }


}
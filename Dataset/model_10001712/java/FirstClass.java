





import java.util.List;
import java.util.ArrayList;

public class FirstClass  {

    private int numberOfSeats;
    private int seatsFilled;



    public FirstClass(
        int numberOfSeats,        int seatsFilled    ) {
        this.numberOfSeats = numberOfSeats;
        this.seatsFilled = seatsFilled;
    }


    public int getNumberofseats() {
        return numberOfSeats;
    }

    public void setNumberofseats(int numberOfSeats) {
        this.numberOfSeats = numberOfSeats;
    }
    public int getSeatsfilled() {
        return seatsFilled;
    }

    public void setSeatsfilled(int seatsFilled) {
        this.seatsFilled = seatsFilled;
    }


}






import java.util.List;
import java.util.ArrayList;

public class button  {

    private int number;





    private elevator elevator;


    public button(
        int number    ) {
        this.number = number;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public elevator getElevator() {
        return elevator;
    }

    public void setElevator(elevator elevator) {
        this.elevator = elevator;
    }

}






import java.util.List;
import java.util.ArrayList;

public class hw3_Floor  {

    private int passengersWaiting;
    private int myFloorNumber;



    public hw3_Floor(
        int passengersWaiting,        int myFloorNumber    ) {
        this.passengersWaiting = passengersWaiting;
        this.myFloorNumber = myFloorNumber;
    }


    public int getPassengerswaiting() {
        return passengersWaiting;
    }

    public void setPassengerswaiting(int passengersWaiting) {
        this.passengersWaiting = passengersWaiting;
    }
    public int getMyfloornumber() {
        return myFloorNumber;
    }

    public void setMyfloornumber(int myFloorNumber) {
        this.myFloorNumber = myFloorNumber;
    }


}






import java.util.List;
import java.util.ArrayList;

public class hw3_Floor  {

    private int myFloorNumber;
    private int passengersWaiting;



    public hw3_Floor(
        int myFloorNumber,        int passengersWaiting    ) {
        this.myFloorNumber = myFloorNumber;
        this.passengersWaiting = passengersWaiting;
    }


    public int getMyfloornumber() {
        return myFloorNumber;
    }

    public void setMyfloornumber(int myFloorNumber) {
        this.myFloorNumber = myFloorNumber;
    }
    public int getPassengerswaiting() {
        return passengersWaiting;
    }

    public void setPassengerswaiting(int passengersWaiting) {
        this.passengersWaiting = passengersWaiting;
    }


}
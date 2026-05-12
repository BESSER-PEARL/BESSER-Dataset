





import java.util.List;
import java.util.ArrayList;

public class Ticket  {

    private int no;





    private CheckStaff checkstaff;




    private Passenger passenger;


    public Ticket(
        int no    ) {
        this.no = no;
    }


    public int getNo() {
        return no;
    }

    public void setNo(int no) {
        this.no = no;
    }

    public CheckStaff getCheckstaff() {
        return checkstaff;
    }

    public void setCheckstaff(CheckStaff checkstaff) {
        this.checkstaff = checkstaff;
    }
    public Passenger getPassenger() {
        return passenger;
    }

    public void setPassenger(Passenger passenger) {
        this.passenger = passenger;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String type;
    private String staffId;
    private String name;





    private ReservationManagementSystem reservationmanagementsystem;


    public Staff(
        String type,        String staffId,        String name    ) {
        this.type = type;
        this.staffId = staffId;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getStaffid() {
        return staffId;
    }

    public void setStaffid(String staffId) {
        this.staffId = staffId;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ReservationManagementSystem getReservationmanagementsystem() {
        return reservationmanagementsystem;
    }

    public void setReservationmanagementsystem(ReservationManagementSystem reservationmanagementsystem) {
        this.reservationmanagementsystem = reservationmanagementsystem;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String name;
    private String staffId;
    private String type;





    private ReservationManagementSystem reservationmanagementsystem;


    public Staff(
        String name,        String staffId,        String type    ) {
        this.name = name;
        this.staffId = staffId;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStaffid() {
        return staffId;
    }

    public void setStaffid(String staffId) {
        this.staffId = staffId;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public ReservationManagementSystem getReservationmanagementsystem() {
        return reservationmanagementsystem;
    }

    public void setReservationmanagementsystem(ReservationManagementSystem reservationmanagementsystem) {
        this.reservationmanagementsystem = reservationmanagementsystem;
    }

}
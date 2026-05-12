





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String type;
    private String name;
    private String staffId;





    private ReservationManagementSystem reservationmanagementsystem;


    public Staff(
        String type,        String name,        String staffId    ) {
        this.type = type;
        this.name = name;
        this.staffId = staffId;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
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

    public ReservationManagementSystem getReservationmanagementsystem() {
        return reservationmanagementsystem;
    }

    public void setReservationmanagementsystem(ReservationManagementSystem reservationmanagementsystem) {
        this.reservationmanagementsystem = reservationmanagementsystem;
    }

}
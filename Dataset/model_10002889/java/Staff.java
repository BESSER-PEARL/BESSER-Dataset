





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String name;
    private String type;
    private String staffId;





    private ReservationManagementSystem reservationmanagementsystem;


    public Staff(
        String name,        String type,        String staffId    ) {
        this.name = name;
        this.type = type;
        this.staffId = staffId;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
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

    public ReservationManagementSystem getReservationmanagementsystem() {
        return reservationmanagementsystem;
    }

    public void setReservationmanagementsystem(ReservationManagementSystem reservationmanagementsystem) {
        this.reservationmanagementsystem = reservationmanagementsystem;
    }

}
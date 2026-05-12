





import java.util.List;
import java.util.ArrayList;

public class StaffUI  {






    private List<Staff> staffs;




    private List<ReservationManagementSystem> reservationmanagementsystems;


    public StaffUI(
    ) {
        this.staffs = new ArrayList<>();
        this.reservationmanagementsystems = new ArrayList<>();
    }

    public StaffUI(
        ArrayList<Staff> staffs,        ArrayList<ReservationManagementSystem> reservationmanagementsystems    ) {
        this.staffs = staffs;
        this.reservationmanagementsystems = reservationmanagementsystems;
    }


    public List<Staff> getStaffs() {
        return staffs;
    }

    public void addStaff(Staff staff) {
        this.staffs.add(staff);
    }
    public List<ReservationManagementSystem> getReservationmanagementsystems() {
        return reservationmanagementsystems;
    }

    public void addReservationmanagementsystem(Reservationmanagementsystem reservationmanagementsystem) {
        this.reservationmanagementsystems.add(reservationmanagementsystem);
    }

}
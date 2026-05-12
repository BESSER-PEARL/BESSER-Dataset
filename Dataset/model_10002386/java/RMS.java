





import java.util.List;
import java.util.ArrayList;

public class RMS  {

    private String bookings;





    private List<Staff> staffs;


    public RMS(
        String bookings    ) {
        this.bookings = bookings;
        this.staffs = new ArrayList<>();
    }

    public RMS(
        String bookings        ArrayList<Staff> staffs    ) {
        this.bookings = bookings;
        this.staffs = staffs;
    }

    public String getBookings() {
        return bookings;
    }

    public void setBookings(String bookings) {
        this.bookings = bookings;
    }

    public List<Staff> getStaffs() {
        return staffs;
    }

    public void addStaff(Staff staff) {
        this.staffs.add(staff);
    }

}
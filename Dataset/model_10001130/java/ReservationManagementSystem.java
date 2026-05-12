





import java.util.List;
import java.util.ArrayList;

public class ReservationManagementSystem  {

    private String bookings;





    private List<CustomerUI> customeruis;




    private List<Staff> staffs;


    public ReservationManagementSystem(
        String bookings    ) {
        this.bookings = bookings;
        this.customeruis = new ArrayList<>();
        this.staffs = new ArrayList<>();
    }

    public ReservationManagementSystem(
        String bookings        ArrayList<CustomerUI> customeruis,        ArrayList<Staff> staffs    ) {
        this.bookings = bookings;
        this.customeruis = customeruis;
        this.staffs = staffs;
    }

    public String getBookings() {
        return bookings;
    }

    public void setBookings(String bookings) {
        this.bookings = bookings;
    }

    public List<CustomerUI> getCustomeruis() {
        return customeruis;
    }

    public void addCustomerui(Customerui customerui) {
        this.customeruis.add(customerui);
    }
    public List<Staff> getStaffs() {
        return staffs;
    }

    public void addStaff(Staff staff) {
        this.staffs.add(staff);
    }

}
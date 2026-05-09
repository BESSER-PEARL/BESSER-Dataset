




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Classes_mdsdBooking_Booking  {

    private LocalDate dateTo;
    private String customerName;
    private int roomNumber;
    private String petName;
    private boolean isCheckedIn;
    private String customerEmail;
    private LocalDate dateFrom;
    private String bill_Id;
    private String bookingId;
    private boolean isCheckedOut;





    private Meal meal;




    private List<Service> services;


    public Classes_mdsdBooking_Booking(
        LocalDate dateTo,        String customerName,        int roomNumber,        String petName,        boolean isCheckedIn,        String customerEmail,        LocalDate dateFrom,        String bill_Id,        String bookingId,        boolean isCheckedOut    ) {
        this.dateTo = dateTo;
        this.customerName = customerName;
        this.roomNumber = roomNumber;
        this.petName = petName;
        this.isCheckedIn = isCheckedIn;
        this.customerEmail = customerEmail;
        this.dateFrom = dateFrom;
        this.bill_Id = bill_Id;
        this.bookingId = bookingId;
        this.isCheckedOut = isCheckedOut;
        this.services = new ArrayList<>();
    }

    public Classes_mdsdBooking_Booking(
        LocalDate dateTo,        String customerName,        int roomNumber,        String petName,        boolean isCheckedIn,        String customerEmail,        LocalDate dateFrom,        String bill_Id,        String bookingId,        boolean isCheckedOut        ArrayList<Service> services    ) {
        this.dateTo = dateTo;
        this.customerName = customerName;
        this.roomNumber = roomNumber;
        this.petName = petName;
        this.isCheckedIn = isCheckedIn;
        this.customerEmail = customerEmail;
        this.dateFrom = dateFrom;
        this.bill_Id = bill_Id;
        this.bookingId = bookingId;
        this.isCheckedOut = isCheckedOut;
        this.services = services;
    }

    public LocalDate getDateto() {
        return dateTo;
    }

    public void setDateto(LocalDate dateTo) {
        this.dateTo = dateTo;
    }
    public String getCustomername() {
        return customerName;
    }

    public void setCustomername(String customerName) {
        this.customerName = customerName;
    }
    public int getRoomnumber() {
        return roomNumber;
    }

    public void setRoomnumber(int roomNumber) {
        this.roomNumber = roomNumber;
    }
    public String getPetname() {
        return petName;
    }

    public void setPetname(String petName) {
        this.petName = petName;
    }
    public boolean getIscheckedin() {
        return isCheckedIn;
    }

    public void setIscheckedin(boolean isCheckedIn) {
        this.isCheckedIn = isCheckedIn;
    }
    public String getCustomeremail() {
        return customerEmail;
    }

    public void setCustomeremail(String customerEmail) {
        this.customerEmail = customerEmail;
    }
    public LocalDate getDatefrom() {
        return dateFrom;
    }

    public void setDatefrom(LocalDate dateFrom) {
        this.dateFrom = dateFrom;
    }
    public String getBill_id() {
        return bill_Id;
    }

    public void setBill_id(String bill_Id) {
        this.bill_Id = bill_Id;
    }
    public String getBookingid() {
        return bookingId;
    }

    public void setBookingid(String bookingId) {
        this.bookingId = bookingId;
    }
    public boolean getIscheckedout() {
        return isCheckedOut;
    }

    public void setIscheckedout(boolean isCheckedOut) {
        this.isCheckedOut = isCheckedOut;
    }

    public Meal getMeal() {
        return meal;
    }

    public void setMeal(Meal meal) {
        this.meal = meal;
    }
    public List<Service> getServices() {
        return services;
    }

    public void addService(Service service) {
        this.services.add(service);
    }

}
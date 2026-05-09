




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Classes_Booking  {

    private LocalDate checkIn;
    private String numberOfGuests;
    private String bookingID;
    private LocalDate checkOut;





    private Classes_Customer classes_customer;




    private Classes_IBookingManagementImpl classes_ibookingmanagementimpl;




    private Classes_Bill classes_bill;




    private Classes_Customer classes_customer;




    private Classes_IBookingManagementImpl classes_ibookingmanagementimpl;




    private Classes_Room classes_room;




    private List<Classes_Room> classes_rooms;




    private Classes_IBookingManagementImpl classes_ibookingmanagementimpl;




    private Classes_IBookingManagementImpl classes_ibookingmanagementimpl;


    public Classes_Booking(
        LocalDate checkIn,        String numberOfGuests,        String bookingID,        LocalDate checkOut    ) {
        this.checkIn = checkIn;
        this.numberOfGuests = numberOfGuests;
        this.bookingID = bookingID;
        this.checkOut = checkOut;
        this.classes_rooms = new ArrayList<>();
    }

    public Classes_Booking(
        LocalDate checkIn,        String numberOfGuests,        String bookingID,        LocalDate checkOut        ArrayList<Classes_Room> classes_rooms    ) {
        this.checkIn = checkIn;
        this.numberOfGuests = numberOfGuests;
        this.bookingID = bookingID;
        this.checkOut = checkOut;
        this.classes_rooms = classes_rooms;
    }

    public LocalDate getCheckin() {
        return checkIn;
    }

    public void setCheckin(LocalDate checkIn) {
        this.checkIn = checkIn;
    }
    public String getNumberofguests() {
        return numberOfGuests;
    }

    public void setNumberofguests(String numberOfGuests) {
        this.numberOfGuests = numberOfGuests;
    }
    public String getBookingid() {
        return bookingID;
    }

    public void setBookingid(String bookingID) {
        this.bookingID = bookingID;
    }
    public LocalDate getCheckout() {
        return checkOut;
    }

    public void setCheckout(LocalDate checkOut) {
        this.checkOut = checkOut;
    }

    public Classes_Customer getClasses_customer() {
        return classes_customer;
    }

    public void setClasses_customer(Classes_Customer classes_customer) {
        this.classes_customer = classes_customer;
    }
    public Classes_IBookingManagementImpl getClasses_ibookingmanagementimpl() {
        return classes_ibookingmanagementimpl;
    }

    public void setClasses_ibookingmanagementimpl(Classes_IBookingManagementImpl classes_ibookingmanagementimpl) {
        this.classes_ibookingmanagementimpl = classes_ibookingmanagementimpl;
    }
    public Classes_Bill getClasses_bill() {
        return classes_bill;
    }

    public void setClasses_bill(Classes_Bill classes_bill) {
        this.classes_bill = classes_bill;
    }
    public Classes_Customer getClasses_customer() {
        return classes_customer;
    }

    public void setClasses_customer(Classes_Customer classes_customer) {
        this.classes_customer = classes_customer;
    }
    public Classes_IBookingManagementImpl getClasses_ibookingmanagementimpl() {
        return classes_ibookingmanagementimpl;
    }

    public void setClasses_ibookingmanagementimpl(Classes_IBookingManagementImpl classes_ibookingmanagementimpl) {
        this.classes_ibookingmanagementimpl = classes_ibookingmanagementimpl;
    }
    public Classes_Room getClasses_room() {
        return classes_room;
    }

    public void setClasses_room(Classes_Room classes_room) {
        this.classes_room = classes_room;
    }
    public List<Classes_Room> getClasses_rooms() {
        return classes_rooms;
    }

    public void addClasses_room(Classes_room classes_room) {
        this.classes_rooms.add(classes_room);
    }
    public Classes_IBookingManagementImpl getClasses_ibookingmanagementimpl() {
        return classes_ibookingmanagementimpl;
    }

    public void setClasses_ibookingmanagementimpl(Classes_IBookingManagementImpl classes_ibookingmanagementimpl) {
        this.classes_ibookingmanagementimpl = classes_ibookingmanagementimpl;
    }
    public Classes_IBookingManagementImpl getClasses_ibookingmanagementimpl() {
        return classes_ibookingmanagementimpl;
    }

    public void setClasses_ibookingmanagementimpl(Classes_IBookingManagementImpl classes_ibookingmanagementimpl) {
        this.classes_ibookingmanagementimpl = classes_ibookingmanagementimpl;
    }

}
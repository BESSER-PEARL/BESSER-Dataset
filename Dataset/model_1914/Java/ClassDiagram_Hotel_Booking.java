




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Hotel_Booking  {

    private boolean checkedIn;
    private LocalDate endDate;
    private float price;
    private int bookingID;
    private LocalDate startDate;





    private ClassDiagram_Company_Hotel classdiagram_company_hotel;




    private ClassDiagram_Company_GuestRecord classdiagram_company_guestrecord;




    private List<ClassDiagram_Hotel_Room> classdiagram_hotel_rooms;


    public ClassDiagram_Hotel_Booking(
        boolean checkedIn,        LocalDate endDate,        float price,        int bookingID,        LocalDate startDate    ) {
        this.checkedIn = checkedIn;
        this.endDate = endDate;
        this.price = price;
        this.bookingID = bookingID;
        this.startDate = startDate;
        this.classdiagram_hotel_rooms = new ArrayList<>();
    }

    public ClassDiagram_Hotel_Booking(
        boolean checkedIn,        LocalDate endDate,        float price,        int bookingID,        LocalDate startDate        ArrayList<ClassDiagram_Hotel_Room> classdiagram_hotel_rooms    ) {
        this.checkedIn = checkedIn;
        this.endDate = endDate;
        this.price = price;
        this.bookingID = bookingID;
        this.startDate = startDate;
        this.classdiagram_hotel_rooms = classdiagram_hotel_rooms;
    }

    public boolean getCheckedin() {
        return checkedIn;
    }

    public void setCheckedin(boolean checkedIn) {
        this.checkedIn = checkedIn;
    }
    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public int getBookingid() {
        return bookingID;
    }

    public void setBookingid(int bookingID) {
        this.bookingID = bookingID;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }

    public ClassDiagram_Company_Hotel getClassdiagram_company_hotel() {
        return classdiagram_company_hotel;
    }

    public void setClassdiagram_company_hotel(ClassDiagram_Company_Hotel classdiagram_company_hotel) {
        this.classdiagram_company_hotel = classdiagram_company_hotel;
    }
    public ClassDiagram_Company_GuestRecord getClassdiagram_company_guestrecord() {
        return classdiagram_company_guestrecord;
    }

    public void setClassdiagram_company_guestrecord(ClassDiagram_Company_GuestRecord classdiagram_company_guestrecord) {
        this.classdiagram_company_guestrecord = classdiagram_company_guestrecord;
    }
    public List<ClassDiagram_Hotel_Room> getClassdiagram_hotel_rooms() {
        return classdiagram_hotel_rooms;
    }

    public void addClassdiagram_hotel_room(Classdiagram_hotel_room classdiagram_hotel_room) {
        this.classdiagram_hotel_rooms.add(classdiagram_hotel_room);
    }

}
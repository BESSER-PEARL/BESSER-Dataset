





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String Payment_Description;
    private String Customer_s_Id;
    private String Payment_Date;
    private String Amount;





    private Customer customer;




    private Booking booking;




    private Room room;


    public Payment(
        String Payment_Description,        String Customer_s_Id,        String Payment_Date,        String Amount    ) {
        this.Payment_Description = Payment_Description;
        this.Customer_s_Id = Customer_s_Id;
        this.Payment_Date = Payment_Date;
        this.Amount = Amount;
    }


    public String getPayment_description() {
        return Payment_Description;
    }

    public void setPayment_description(String Payment_Description) {
        this.Payment_Description = Payment_Description;
    }
    public String getCustomer_s_id() {
        return Customer_s_Id;
    }

    public void setCustomer_s_id(String Customer_s_Id) {
        this.Customer_s_Id = Customer_s_Id;
    }
    public String getPayment_date() {
        return Payment_Date;
    }

    public void setPayment_date(String Payment_Date) {
        this.Payment_Date = Payment_Date;
    }
    public String getAmount() {
        return Amount;
    }

    public void setAmount(String Amount) {
        this.Amount = Amount;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }
    public Room getRoom() {
        return room;
    }

    public void setRoom(Room room) {
        this.room = room;
    }

}
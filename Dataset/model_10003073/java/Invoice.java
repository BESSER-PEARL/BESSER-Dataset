





import java.util.List;
import java.util.ArrayList;

public class Invoice  {

    private String orders;
    private String invoice_id;





    private ReservationManagementSystem reservationmanagementsystem;


    public Invoice(
        String orders,        String invoice_id    ) {
        this.orders = orders;
        this.invoice_id = invoice_id;
    }


    public String getOrders() {
        return orders;
    }

    public void setOrders(String orders) {
        this.orders = orders;
    }
    public String getInvoice_id() {
        return invoice_id;
    }

    public void setInvoice_id(String invoice_id) {
        this.invoice_id = invoice_id;
    }

    public ReservationManagementSystem getReservationmanagementsystem() {
        return reservationmanagementsystem;
    }

    public void setReservationmanagementsystem(ReservationManagementSystem reservationmanagementsystem) {
        this.reservationmanagementsystem = reservationmanagementsystem;
    }

}
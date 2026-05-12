





import java.util.List;
import java.util.ArrayList;

public class Report  {

    private String orders;
    private String report_id;





    private ReservationManagementSystem reservationmanagementsystem;


    public Report(
        String orders,        String report_id    ) {
        this.orders = orders;
        this.report_id = report_id;
    }


    public String getOrders() {
        return orders;
    }

    public void setOrders(String orders) {
        this.orders = orders;
    }
    public String getReport_id() {
        return report_id;
    }

    public void setReport_id(String report_id) {
        this.report_id = report_id;
    }

    public ReservationManagementSystem getReservationmanagementsystem() {
        return reservationmanagementsystem;
    }

    public void setReservationmanagementsystem(ReservationManagementSystem reservationmanagementsystem) {
        this.reservationmanagementsystem = reservationmanagementsystem;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Report  {

    private String report_id;
    private String orders;





    private Reservation_System reservation_system;


    public Report(
        String report_id,        String orders    ) {
        this.report_id = report_id;
        this.orders = orders;
    }


    public String getReport_id() {
        return report_id;
    }

    public void setReport_id(String report_id) {
        this.report_id = report_id;
    }
    public String getOrders() {
        return orders;
    }

    public void setOrders(String orders) {
        this.orders = orders;
    }

    public Reservation_System getReservation_system() {
        return reservation_system;
    }

    public void setReservation_system(Reservation_System reservation_system) {
        this.reservation_system = reservation_system;
    }

}
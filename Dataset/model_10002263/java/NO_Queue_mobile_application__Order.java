





import java.util.List;
import java.util.ArrayList;

public class NO_Queue_mobile_application__Order  {

    private String status;
    private String Number;
    private String shipped;
    private String ordered;
    private String Ship_to;
    private String total;





    private NO_Queue_mobile_application__Account no_queue_mobile_application__account;


    public NO_Queue_mobile_application__Order(
        String status,        String Number,        String shipped,        String ordered,        String Ship_to,        String total    ) {
        this.status = status;
        this.Number = Number;
        this.shipped = shipped;
        this.ordered = ordered;
        this.Ship_to = Ship_to;
        this.total = total;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getNumber() {
        return Number;
    }

    public void setNumber(String Number) {
        this.Number = Number;
    }
    public String getShipped() {
        return shipped;
    }

    public void setShipped(String shipped) {
        this.shipped = shipped;
    }
    public String getOrdered() {
        return ordered;
    }

    public void setOrdered(String ordered) {
        this.ordered = ordered;
    }
    public String getShip_to() {
        return Ship_to;
    }

    public void setShip_to(String Ship_to) {
        this.Ship_to = Ship_to;
    }
    public String getTotal() {
        return total;
    }

    public void setTotal(String total) {
        this.total = total;
    }

    public NO_Queue_mobile_application__Account getNo_queue_mobile_application__account() {
        return no_queue_mobile_application__account;
    }

    public void setNo_queue_mobile_application__account(NO_Queue_mobile_application__Account no_queue_mobile_application__account) {
        this.no_queue_mobile_application__account = no_queue_mobile_application__account;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_System_Order  {

    private String Ship_to;
    private String status;
    private String ordered;
    private String shipped;
    private String Number;
    private String total;



    public Online_Shopping_System_Order(
        String Ship_to,        String status,        String ordered,        String shipped,        String Number,        String total    ) {
        this.Ship_to = Ship_to;
        this.status = status;
        this.ordered = ordered;
        this.shipped = shipped;
        this.Number = Number;
        this.total = total;
    }


    public String getShip_to() {
        return Ship_to;
    }

    public void setShip_to(String Ship_to) {
        this.Ship_to = Ship_to;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getOrdered() {
        return ordered;
    }

    public void setOrdered(String ordered) {
        this.ordered = ordered;
    }
    public String getShipped() {
        return shipped;
    }

    public void setShipped(String shipped) {
        this.shipped = shipped;
    }
    public String getNumber() {
        return Number;
    }

    public void setNumber(String Number) {
        this.Number = Number;
    }
    public String getTotal() {
        return total;
    }

    public void setTotal(String total) {
        this.total = total;
    }


}
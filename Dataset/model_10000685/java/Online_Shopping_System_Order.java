





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_System_Order  {

    private String Ship_to;
    private String ordered;
    private String total;
    private String status;
    private String Number;
    private String shipped;





    private Online_Shopping_System_Account online_shopping_system_account;


    public Online_Shopping_System_Order(
        String Ship_to,        String ordered,        String total,        String status,        String Number,        String shipped    ) {
        this.Ship_to = Ship_to;
        this.ordered = ordered;
        this.total = total;
        this.status = status;
        this.Number = Number;
        this.shipped = shipped;
    }


    public String getShip_to() {
        return Ship_to;
    }

    public void setShip_to(String Ship_to) {
        this.Ship_to = Ship_to;
    }
    public String getOrdered() {
        return ordered;
    }

    public void setOrdered(String ordered) {
        this.ordered = ordered;
    }
    public String getTotal() {
        return total;
    }

    public void setTotal(String total) {
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

    public Online_Shopping_System_Account getOnline_shopping_system_account() {
        return online_shopping_system_account;
    }

    public void setOnline_shopping_system_account(Online_Shopping_System_Account online_shopping_system_account) {
        this.online_shopping_system_account = online_shopping_system_account;
    }

}
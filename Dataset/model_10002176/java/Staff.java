





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private None staffid;
    private None name;





    private Order_management_System order_management_system;


    public Staff(
        None staffid,        None name    ) {
        this.staffid = staffid;
        this.name = name;
    }


    public None getStaffid() {
        return staffid;
    }

    public void setStaffid(None staffid) {
        this.staffid = staffid;
    }
    public None getName() {
        return name;
    }

    public void setName(None name) {
        this.name = name;
    }

    public Order_management_System getOrder_management_system() {
        return order_management_system;
    }

    public void setOrder_management_system(Order_management_System order_management_system) {
        this.order_management_system = order_management_system;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Delivery  {

    private String Type;
    private String Date;
    private String Name;





    private Order order;


    public Delivery(
        String Type,        String Date,        String Name    ) {
        this.Type = Type;
        this.Date = Date;
        this.Name = Name;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int id;
    private String Date;
    private None ProductID;



    public Order(
        int id,        String Date,        None ProductID    ) {
        this.id = id;
        this.Date = Date;
        this.ProductID = ProductID;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public None getProductid() {
        return ProductID;
    }

    public void setProductid(None ProductID) {
        this.ProductID = ProductID;
    }


}
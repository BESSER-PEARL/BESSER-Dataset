





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int Total;
    private String id;



    public Order(
        int Total,        String id    ) {
        this.Total = Total;
        this.id = id;
    }


    public int getTotal() {
        return Total;
    }

    public void setTotal(int Total) {
        this.Total = Total;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}
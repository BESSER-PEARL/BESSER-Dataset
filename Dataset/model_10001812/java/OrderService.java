





import java.util.List;
import java.util.ArrayList;

public class OrderService  {

    private String attribute;



    public OrderService(
        String attribute    ) {
        this.attribute = attribute;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}






import java.util.List;
import java.util.ArrayList;

public class simplepdl_Resource extends ProcessElement {

    private String name;
    private String quantity;



    public simplepdl_Resource(
        String name,        String quantity    ) {
        super(
        );
        this.name = name;
        this.quantity = quantity;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }


}
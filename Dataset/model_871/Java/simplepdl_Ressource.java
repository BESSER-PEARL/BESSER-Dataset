





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Ressource extends ProcessElement {

    private String name;
    private int quantity;



    public simplepdl_Ressource(
        String name,        int quantity    ) {
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
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }


}
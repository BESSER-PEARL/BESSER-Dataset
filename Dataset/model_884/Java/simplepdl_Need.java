





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Need extends ProcessElement {

    private int quantity;





    private simplepdl_Ressource simplepdl_ressource;


    public simplepdl_Need(
        int quantity    ) {
        super(
        );
        this.quantity = quantity;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public simplepdl_Ressource getSimplepdl_ressource() {
        return simplepdl_ressource;
    }

    public void setSimplepdl_ressource(simplepdl_Ressource simplepdl_ressource) {
        this.simplepdl_ressource = simplepdl_ressource;
    }

}
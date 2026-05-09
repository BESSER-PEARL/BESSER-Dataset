





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Ressource extends ProcessElement {

    private int quantity;
    private String name;





    private simplepdl_RessourceLink simplepdl_ressourcelink;


    public simplepdl_Ressource(
        int quantity,        String name    ) {
        super(
        );
        this.quantity = quantity;
        this.name = name;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simplepdl_RessourceLink getSimplepdl_ressourcelink() {
        return simplepdl_ressourcelink;
    }

    public void setSimplepdl_ressourcelink(simplepdl_RessourceLink simplepdl_ressourcelink) {
        this.simplepdl_ressourcelink = simplepdl_ressourcelink;
    }

}






import java.util.List;
import java.util.ArrayList;

public class simplepdl_Ressource extends ProcessElement {

    private String type;
    private int quantity;





    private simplepdl_RessourceConso simplepdl_ressourceconso;


    public simplepdl_Ressource(
        String type,        int quantity    ) {
        super(
        );
        this.type = type;
        this.quantity = quantity;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public simplepdl_RessourceConso getSimplepdl_ressourceconso() {
        return simplepdl_ressourceconso;
    }

    public void setSimplepdl_ressourceconso(simplepdl_RessourceConso simplepdl_ressourceconso) {
        this.simplepdl_ressourceconso = simplepdl_ressourceconso;
    }

}
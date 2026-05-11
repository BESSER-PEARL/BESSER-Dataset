





import java.util.List;
import java.util.ArrayList;

public class crom_l1_composed_Operation extends TypedElement {

    private String operation;





    private crom_l1_composed_Type crom_l1_composed_type;




    private List<crom_l1_composed_Parameter> crom_l1_composed_parameters;




    private crom_l1_composed_Type crom_l1_composed_type;


    public crom_l1_composed_Operation(
        String operation    ) {
        super(
        );
        this.operation = operation;
        this.crom_l1_composed_parameters = new ArrayList<>();
    }

    public crom_l1_composed_Operation(
        String operation        ArrayList<crom_l1_composed_Parameter> crom_l1_composed_parameters    ) {
        this.operation = operation;
        this.crom_l1_composed_parameters = crom_l1_composed_parameters;
    }

    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }

    public crom_l1_composed_Type getCrom_l1_composed_type() {
        return crom_l1_composed_type;
    }

    public void setCrom_l1_composed_type(crom_l1_composed_Type crom_l1_composed_type) {
        this.crom_l1_composed_type = crom_l1_composed_type;
    }
    public List<crom_l1_composed_Parameter> getCrom_l1_composed_parameters() {
        return crom_l1_composed_parameters;
    }

    public void addCrom_l1_composed_parameter(Crom_l1_composed_parameter crom_l1_composed_parameter) {
        this.crom_l1_composed_parameters.add(crom_l1_composed_parameter);
    }
    public crom_l1_composed_Type getCrom_l1_composed_type() {
        return crom_l1_composed_type;
    }

    public void setCrom_l1_composed_type(crom_l1_composed_Type crom_l1_composed_type) {
        this.crom_l1_composed_type = crom_l1_composed_type;
    }

}
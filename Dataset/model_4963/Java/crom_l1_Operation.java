





import java.util.List;
import java.util.ArrayList;

public class crom_l1_Operation extends TypedElement {

    private String operation;





    private List<crom_l1_Parameter> crom_l1_parameters;




    private crom_l1_Type crom_l1_type;




    private crom_l1_Type crom_l1_type;


    public crom_l1_Operation(
        String operation    ) {
        super(
        );
        this.operation = operation;
        this.crom_l1_parameters = new ArrayList<>();
    }

    public crom_l1_Operation(
        String operation        ArrayList<crom_l1_Parameter> crom_l1_parameters    ) {
        this.operation = operation;
        this.crom_l1_parameters = crom_l1_parameters;
    }

    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }

    public List<crom_l1_Parameter> getCrom_l1_parameters() {
        return crom_l1_parameters;
    }

    public void addCrom_l1_parameter(Crom_l1_parameter crom_l1_parameter) {
        this.crom_l1_parameters.add(crom_l1_parameter);
    }
    public crom_l1_Type getCrom_l1_type() {
        return crom_l1_type;
    }

    public void setCrom_l1_type(crom_l1_Type crom_l1_type) {
        this.crom_l1_type = crom_l1_type;
    }
    public crom_l1_Type getCrom_l1_type() {
        return crom_l1_type;
    }

    public void setCrom_l1_type(crom_l1_Type crom_l1_type) {
        this.crom_l1_type = crom_l1_type;
    }

}
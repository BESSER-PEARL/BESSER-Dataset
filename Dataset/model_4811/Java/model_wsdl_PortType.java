





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_PortType extends wsdl_IPortType, wsdl_ExtensibleElement {

    private String qName;
    private boolean undefined;





    private List<Operation> operations;


    public model_wsdl_PortType(
        String qName,        boolean undefined    ) {
        super(
        );
        this.qName = qName;
        this.undefined = undefined;
        this.operations = new ArrayList<>();
    }

    public model_wsdl_PortType(
        String qName,        boolean undefined        ArrayList<Operation> operations    ) {
        this.qName = qName;
        this.undefined = undefined;
        this.operations = operations;
    }

    public String getQname() {
        return qName;
    }

    public void setQname(String qName) {
        this.qName = qName;
    }
    public boolean getUndefined() {
        return undefined;
    }

    public void setUndefined(boolean undefined) {
        this.undefined = undefined;
    }

    public List<Operation> getOperations() {
        return operations;
    }

    public void addOperation(Operation operation) {
        this.operations.add(operation);
    }

}
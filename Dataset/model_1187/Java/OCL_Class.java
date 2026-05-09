





import java.util.List;
import java.util.ArrayList;

public class OCL_Class extends Type {

    private String isAbstract;





    private List<Property> propertys;




    private List<Operation> operations;


    public OCL_Class(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.propertys = new ArrayList<>();
        this.operations = new ArrayList<>();
    }

    public OCL_Class(
        String isAbstract        ArrayList<Property> propertys,        ArrayList<Operation> operations    ) {
        this.isAbstract = isAbstract;
        this.propertys = propertys;
        this.operations = operations;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }
    public List<Operation> getOperations() {
        return operations;
    }

    public void addOperation(Operation operation) {
        this.operations.add(operation);
    }

}
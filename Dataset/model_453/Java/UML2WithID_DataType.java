





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_DataType extends Classifier {






    private UML2WithID_Property uml2withid_property;




    private List<UML2WithID_Operation> uml2withid_operations;




    private UML2WithID_Operation uml2withid_operation;




    private List<UML2WithID_Property> uml2withid_propertys;


    public UML2WithID_DataType(
    ) {
        super(
        );
        this.uml2withid_operations = new ArrayList<>();
        this.uml2withid_propertys = new ArrayList<>();
    }

    public UML2WithID_DataType(
        ArrayList<UML2WithID_Operation> uml2withid_operations,        ArrayList<UML2WithID_Property> uml2withid_propertys    ) {
        this.uml2withid_operations = uml2withid_operations;
        this.uml2withid_propertys = uml2withid_propertys;
    }


    public UML2WithID_Property getUml2withid_property() {
        return uml2withid_property;
    }

    public void setUml2withid_property(UML2WithID_Property uml2withid_property) {
        this.uml2withid_property = uml2withid_property;
    }
    public List<UML2WithID_Operation> getUml2withid_operations() {
        return uml2withid_operations;
    }

    public void addUml2withid_operation(Uml2withid_operation uml2withid_operation) {
        this.uml2withid_operations.add(uml2withid_operation);
    }
    public UML2WithID_Operation getUml2withid_operation() {
        return uml2withid_operation;
    }

    public void setUml2withid_operation(UML2WithID_Operation uml2withid_operation) {
        this.uml2withid_operation = uml2withid_operation;
    }
    public List<UML2WithID_Property> getUml2withid_propertys() {
        return uml2withid_propertys;
    }

    public void addUml2withid_property(Uml2withid_property uml2withid_property) {
        this.uml2withid_propertys.add(uml2withid_property);
    }

}
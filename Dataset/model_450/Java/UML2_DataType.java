





import java.util.List;
import java.util.ArrayList;

public class UML2_DataType extends Classifier {






    private List<UML2_Operation> uml2_operations;




    private List<UML2_Property> uml2_propertys;




    private UML2_Property uml2_property;




    private UML2_Operation uml2_operation;


    public UML2_DataType(
    ) {
        super(
        );
        this.uml2_operations = new ArrayList<>();
        this.uml2_propertys = new ArrayList<>();
    }

    public UML2_DataType(
        ArrayList<UML2_Operation> uml2_operations,        ArrayList<UML2_Property> uml2_propertys    ) {
        this.uml2_operations = uml2_operations;
        this.uml2_propertys = uml2_propertys;
    }


    public List<UML2_Operation> getUml2_operations() {
        return uml2_operations;
    }

    public void addUml2_operation(Uml2_operation uml2_operation) {
        this.uml2_operations.add(uml2_operation);
    }
    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }
    public UML2_Property getUml2_property() {
        return uml2_property;
    }

    public void setUml2_property(UML2_Property uml2_property) {
        this.uml2_property = uml2_property;
    }
    public UML2_Operation getUml2_operation() {
        return uml2_operation;
    }

    public void setUml2_operation(UML2_Operation uml2_operation) {
        this.uml2_operation = uml2_operation;
    }

}
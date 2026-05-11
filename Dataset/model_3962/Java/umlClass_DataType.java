





import java.util.List;
import java.util.ArrayList;

public class umlClass_DataType extends Classifier {






    private umlClass_Operation umlclass_operation;




    private List<umlClass_Operation> umlclass_operations;




    private umlClass_Property umlclass_property;




    private List<umlClass_Property> umlclass_propertys;


    public umlClass_DataType(
    ) {
        super(
        );
        this.umlclass_operations = new ArrayList<>();
        this.umlclass_propertys = new ArrayList<>();
    }

    public umlClass_DataType(
        ArrayList<umlClass_Operation> umlclass_operations,        ArrayList<umlClass_Property> umlclass_propertys    ) {
        this.umlclass_operations = umlclass_operations;
        this.umlclass_propertys = umlclass_propertys;
    }


    public umlClass_Operation getUmlclass_operation() {
        return umlclass_operation;
    }

    public void setUmlclass_operation(umlClass_Operation umlclass_operation) {
        this.umlclass_operation = umlclass_operation;
    }
    public List<umlClass_Operation> getUmlclass_operations() {
        return umlclass_operations;
    }

    public void addUmlclass_operation(Umlclass_operation umlclass_operation) {
        this.umlclass_operations.add(umlclass_operation);
    }
    public umlClass_Property getUmlclass_property() {
        return umlclass_property;
    }

    public void setUmlclass_property(umlClass_Property umlclass_property) {
        this.umlclass_property = umlclass_property;
    }
    public List<umlClass_Property> getUmlclass_propertys() {
        return umlclass_propertys;
    }

    public void addUmlclass_property(Umlclass_property umlclass_property) {
        this.umlclass_propertys.add(umlclass_property);
    }

}
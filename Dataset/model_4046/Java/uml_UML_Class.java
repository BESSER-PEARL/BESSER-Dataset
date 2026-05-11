





import java.util.List;
import java.util.ArrayList;

public class uml_UML_Class extends UML_BehavioredClassifier {






    private List<uml_UML_Property> uml_uml_propertys;




    private List<uml_UML_Operation> uml_uml_operations;


    public uml_UML_Class(
    ) {
        super(
        );
        this.uml_uml_propertys = new ArrayList<>();
        this.uml_uml_operations = new ArrayList<>();
    }

    public uml_UML_Class(
        ArrayList<uml_UML_Property> uml_uml_propertys,        ArrayList<uml_UML_Operation> uml_uml_operations    ) {
        this.uml_uml_propertys = uml_uml_propertys;
        this.uml_uml_operations = uml_uml_operations;
    }


    public List<uml_UML_Property> getUml_uml_propertys() {
        return uml_uml_propertys;
    }

    public void addUml_uml_property(Uml_uml_property uml_uml_property) {
        this.uml_uml_propertys.add(uml_uml_property);
    }
    public List<uml_UML_Operation> getUml_uml_operations() {
        return uml_uml_operations;
    }

    public void addUml_uml_operation(Uml_uml_operation uml_uml_operation) {
        this.uml_uml_operations.add(uml_uml_operation);
    }

}






import java.util.List;
import java.util.ArrayList;

public class umlsimp_Class extends ModelElement {






    private List<umlsimp_Operation> umlsimp_operations;




    private umlsimp_Property umlsimp_property;




    private umlsimp_Operation umlsimp_operation;




    private List<umlsimp_Property> umlsimp_propertys;


    public umlsimp_Class(
    ) {
        super(
        );
        this.umlsimp_operations = new ArrayList<>();
        this.umlsimp_propertys = new ArrayList<>();
    }

    public umlsimp_Class(
        ArrayList<umlsimp_Operation> umlsimp_operations,        ArrayList<umlsimp_Property> umlsimp_propertys    ) {
        this.umlsimp_operations = umlsimp_operations;
        this.umlsimp_propertys = umlsimp_propertys;
    }


    public List<umlsimp_Operation> getUmlsimp_operations() {
        return umlsimp_operations;
    }

    public void addUmlsimp_operation(Umlsimp_operation umlsimp_operation) {
        this.umlsimp_operations.add(umlsimp_operation);
    }
    public umlsimp_Property getUmlsimp_property() {
        return umlsimp_property;
    }

    public void setUmlsimp_property(umlsimp_Property umlsimp_property) {
        this.umlsimp_property = umlsimp_property;
    }
    public umlsimp_Operation getUmlsimp_operation() {
        return umlsimp_operation;
    }

    public void setUmlsimp_operation(umlsimp_Operation umlsimp_operation) {
        this.umlsimp_operation = umlsimp_operation;
    }
    public List<umlsimp_Property> getUmlsimp_propertys() {
        return umlsimp_propertys;
    }

    public void addUmlsimp_property(Umlsimp_property umlsimp_property) {
        this.umlsimp_propertys.add(umlsimp_property);
    }

}
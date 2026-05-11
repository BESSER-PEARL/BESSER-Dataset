





import java.util.List;
import java.util.ArrayList;

public class types_ServiceType extends UserType {






    private List<types_Property> types_propertys;




    private List<types_Operation> types_operations;


    public types_ServiceType(
    ) {
        super(
        );
        this.types_propertys = new ArrayList<>();
        this.types_operations = new ArrayList<>();
    }

    public types_ServiceType(
        ArrayList<types_Property> types_propertys,        ArrayList<types_Operation> types_operations    ) {
        this.types_propertys = types_propertys;
        this.types_operations = types_operations;
    }


    public List<types_Property> getTypes_propertys() {
        return types_propertys;
    }

    public void addTypes_property(Types_property types_property) {
        this.types_propertys.add(types_property);
    }
    public List<types_Operation> getTypes_operations() {
        return types_operations;
    }

    public void addTypes_operation(Types_operation types_operation) {
        this.types_operations.add(types_operation);
    }

}
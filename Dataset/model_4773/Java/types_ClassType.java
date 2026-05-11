





import java.util.List;
import java.util.ArrayList;

public class types_ClassType extends UserType {






    private types_ClassType types_classtype;




    private List<types_Property> types_propertys;


    public types_ClassType(
    ) {
        super(
        );
        this.types_propertys = new ArrayList<>();
    }

    public types_ClassType(
        ArrayList<types_Property> types_propertys    ) {
        this.types_propertys = types_propertys;
    }


    public types_ClassType getTypes_classtype() {
        return types_classtype;
    }

    public void setTypes_classtype(types_ClassType types_classtype) {
        this.types_classtype = types_classtype;
    }
    public List<types_Property> getTypes_propertys() {
        return types_propertys;
    }

    public void addTypes_property(Types_property types_property) {
        this.types_propertys.add(types_property);
    }

}
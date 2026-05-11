





import java.util.List;
import java.util.ArrayList;

public class types_AnnotationType extends Type {






    private List<types_Property> types_propertys;


    public types_AnnotationType(
    ) {
        super(
        );
        this.types_propertys = new ArrayList<>();
    }

    public types_AnnotationType(
        ArrayList<types_Property> types_propertys    ) {
        this.types_propertys = types_propertys;
    }


    public List<types_Property> getTypes_propertys() {
        return types_propertys;
    }

    public void addTypes_property(Types_property types_property) {
        this.types_propertys.add(types_property);
    }

}
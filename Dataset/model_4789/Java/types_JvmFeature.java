





import java.util.List;
import java.util.ArrayList;

public class types_JvmFeature extends JvmMember {






    private List<types_JvmGenericType> types_jvmgenerictypes;


    public types_JvmFeature(
    ) {
        super(
        );
        this.types_jvmgenerictypes = new ArrayList<>();
    }

    public types_JvmFeature(
        ArrayList<types_JvmGenericType> types_jvmgenerictypes    ) {
        this.types_jvmgenerictypes = types_jvmgenerictypes;
    }


    public List<types_JvmGenericType> getTypes_jvmgenerictypes() {
        return types_jvmgenerictypes;
    }

    public void addTypes_jvmgenerictype(Types_jvmgenerictype types_jvmgenerictype) {
        this.types_jvmgenerictypes.add(types_jvmgenerictype);
    }

}
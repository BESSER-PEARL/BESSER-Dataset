





import java.util.List;
import java.util.ArrayList;

public class types_JvmParameterizedTypeReference extends JvmTypeReference {






    private types_JvmInnerTypeReference types_jvminnertypereference;




    private List<types_JvmTypeReference> types_jvmtypereferences;




    private types_JvmType types_jvmtype;


    public types_JvmParameterizedTypeReference(
    ) {
        super(
        );
        this.types_jvmtypereferences = new ArrayList<>();
    }

    public types_JvmParameterizedTypeReference(
        ArrayList<types_JvmTypeReference> types_jvmtypereferences    ) {
        this.types_jvmtypereferences = types_jvmtypereferences;
    }


    public types_JvmInnerTypeReference getTypes_jvminnertypereference() {
        return types_jvminnertypereference;
    }

    public void setTypes_jvminnertypereference(types_JvmInnerTypeReference types_jvminnertypereference) {
        this.types_jvminnertypereference = types_jvminnertypereference;
    }
    public List<types_JvmTypeReference> getTypes_jvmtypereferences() {
        return types_jvmtypereferences;
    }

    public void addTypes_jvmtypereference(Types_jvmtypereference types_jvmtypereference) {
        this.types_jvmtypereferences.add(types_jvmtypereference);
    }
    public types_JvmType getTypes_jvmtype() {
        return types_jvmtype;
    }

    public void setTypes_jvmtype(types_JvmType types_jvmtype) {
        this.types_jvmtype = types_jvmtype;
    }

}
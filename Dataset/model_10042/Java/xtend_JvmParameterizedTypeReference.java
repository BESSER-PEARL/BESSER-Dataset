





import java.util.List;
import java.util.ArrayList;

public class xtend_JvmParameterizedTypeReference extends JvmTypeReference {






    private List<xtend_JvmTypeReference> xtend_jvmtypereferences;




    private xtend_JvmType xtend_jvmtype;


    public xtend_JvmParameterizedTypeReference(
    ) {
        super(
        );
        this.xtend_jvmtypereferences = new ArrayList<>();
    }

    public xtend_JvmParameterizedTypeReference(
        ArrayList<xtend_JvmTypeReference> xtend_jvmtypereferences    ) {
        this.xtend_jvmtypereferences = xtend_jvmtypereferences;
    }


    public List<xtend_JvmTypeReference> getXtend_jvmtypereferences() {
        return xtend_jvmtypereferences;
    }

    public void addXtend_jvmtypereference(Xtend_jvmtypereference xtend_jvmtypereference) {
        this.xtend_jvmtypereferences.add(xtend_jvmtypereference);
    }
    public xtend_JvmType getXtend_jvmtype() {
        return xtend_jvmtype;
    }

    public void setXtend_jvmtype(xtend_JvmType xtend_jvmtype) {
        this.xtend_jvmtype = xtend_jvmtype;
    }

}






import java.util.List;
import java.util.ArrayList;

public class xtend_JvmTypeAnnotationValue extends JvmAnnotationValue {






    private List<xtend_JvmTypeReference> xtend_jvmtypereferences;


    public xtend_JvmTypeAnnotationValue(
    ) {
        super(
        );
        this.xtend_jvmtypereferences = new ArrayList<>();
    }

    public xtend_JvmTypeAnnotationValue(
        ArrayList<xtend_JvmTypeReference> xtend_jvmtypereferences    ) {
        this.xtend_jvmtypereferences = xtend_jvmtypereferences;
    }


    public List<xtend_JvmTypeReference> getXtend_jvmtypereferences() {
        return xtend_jvmtypereferences;
    }

    public void addXtend_jvmtypereference(Xtend_jvmtypereference xtend_jvmtypereference) {
        this.xtend_jvmtypereferences.add(xtend_jvmtypereference);
    }

}






import java.util.List;
import java.util.ArrayList;

public class model_ss_XtendInterface extends XtendTypeDeclaration {






    private List<JvmTypeParameter> jvmtypeparameters;




    private List<JvmTypeReference> jvmtypereferences;


    public model_ss_XtendInterface(
    ) {
        super(
        );
        this.jvmtypeparameters = new ArrayList<>();
        this.jvmtypereferences = new ArrayList<>();
    }

    public model_ss_XtendInterface(
        ArrayList<JvmTypeParameter> jvmtypeparameters,        ArrayList<JvmTypeReference> jvmtypereferences    ) {
        this.jvmtypeparameters = jvmtypeparameters;
        this.jvmtypereferences = jvmtypereferences;
    }


    public List<JvmTypeParameter> getJvmtypeparameters() {
        return jvmtypeparameters;
    }

    public void addJvmtypeparameter(Jvmtypeparameter jvmtypeparameter) {
        this.jvmtypeparameters.add(jvmtypeparameter);
    }
    public List<JvmTypeReference> getJvmtypereferences() {
        return jvmtypereferences;
    }

    public void addJvmtypereference(Jvmtypereference jvmtypereference) {
        this.jvmtypereferences.add(jvmtypereference);
    }

}
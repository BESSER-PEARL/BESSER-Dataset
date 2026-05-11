





import java.util.List;
import java.util.ArrayList;

public class model_ss_XtendClass extends XtendTypeDeclaration {






    private List<JvmTypeParameter> jvmtypeparameters;




    private JvmTypeReference jvmtypereference;




    private List<JvmTypeReference> jvmtypereferences;


    public model_ss_XtendClass(
    ) {
        super(
        );
        this.jvmtypeparameters = new ArrayList<>();
        this.jvmtypereferences = new ArrayList<>();
    }

    public model_ss_XtendClass(
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
    public JvmTypeReference getJvmtypereference() {
        return jvmtypereference;
    }

    public void setJvmtypereference(JvmTypeReference jvmtypereference) {
        this.jvmtypereference = jvmtypereference;
    }
    public List<JvmTypeReference> getJvmtypereferences() {
        return jvmtypereferences;
    }

    public void addJvmtypereference(Jvmtypereference jvmtypereference) {
        this.jvmtypereferences.add(jvmtypereference);
    }

}
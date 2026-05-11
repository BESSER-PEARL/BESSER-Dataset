





import java.util.List;
import java.util.ArrayList;

public class model_ss_XtendDelegate extends XtendTypeDeclaration {






    private List<JvmTypeReference> jvmtypereferences;




    private JvmTypeReference jvmtypereference;




    private List<JvmTypeParameter> jvmtypeparameters;


    public model_ss_XtendDelegate(
    ) {
        super(
        );
        this.jvmtypereferences = new ArrayList<>();
        this.jvmtypeparameters = new ArrayList<>();
    }

    public model_ss_XtendDelegate(
        ArrayList<JvmTypeReference> jvmtypereferences,        ArrayList<JvmTypeParameter> jvmtypeparameters    ) {
        this.jvmtypereferences = jvmtypereferences;
        this.jvmtypeparameters = jvmtypeparameters;
    }


    public List<JvmTypeReference> getJvmtypereferences() {
        return jvmtypereferences;
    }

    public void addJvmtypereference(Jvmtypereference jvmtypereference) {
        this.jvmtypereferences.add(jvmtypereference);
    }
    public JvmTypeReference getJvmtypereference() {
        return jvmtypereference;
    }

    public void setJvmtypereference(JvmTypeReference jvmtypereference) {
        this.jvmtypereference = jvmtypereference;
    }
    public List<JvmTypeParameter> getJvmtypeparameters() {
        return jvmtypeparameters;
    }

    public void addJvmtypeparameter(Jvmtypeparameter jvmtypeparameter) {
        this.jvmtypeparameters.add(jvmtypeparameter);
    }

}
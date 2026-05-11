





import java.util.List;
import java.util.ArrayList;

public class model_ss_XtendFunction extends XtendMember {

    private String name;





    private List<JvmTypeParameter> jvmtypeparameters;




    private XExpression xexpression;




    private List<JvmTypeReference> jvmtypereferences;




    private JvmTypeReference jvmtypereference;


    public model_ss_XtendFunction(
        String name    ) {
        super(
        );
        this.name = name;
        this.jvmtypeparameters = new ArrayList<>();
        this.jvmtypereferences = new ArrayList<>();
    }

    public model_ss_XtendFunction(
        String name        ArrayList<JvmTypeParameter> jvmtypeparameters,        ArrayList<JvmTypeReference> jvmtypereferences    ) {
        this.name = name;
        this.jvmtypeparameters = jvmtypeparameters;
        this.jvmtypereferences = jvmtypereferences;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<JvmTypeParameter> getJvmtypeparameters() {
        return jvmtypeparameters;
    }

    public void addJvmtypeparameter(Jvmtypeparameter jvmtypeparameter) {
        this.jvmtypeparameters.add(jvmtypeparameter);
    }
    public XExpression getXexpression() {
        return xexpression;
    }

    public void setXexpression(XExpression xexpression) {
        this.xexpression = xexpression;
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

}
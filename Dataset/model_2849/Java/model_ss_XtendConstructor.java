





import java.util.List;
import java.util.ArrayList;

public class model_ss_XtendConstructor extends XtendMember {






    private List<JvmTypeReference> jvmtypereferences;




    private XExpression xexpression;




    private List<JvmTypeParameter> jvmtypeparameters;


    public model_ss_XtendConstructor(
    ) {
        super(
        );
        this.jvmtypereferences = new ArrayList<>();
        this.jvmtypeparameters = new ArrayList<>();
    }

    public model_ss_XtendConstructor(
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
    public XExpression getXexpression() {
        return xexpression;
    }

    public void setXexpression(XExpression xexpression) {
        this.xexpression = xexpression;
    }
    public List<JvmTypeParameter> getJvmtypeparameters() {
        return jvmtypeparameters;
    }

    public void addJvmtypeparameter(Jvmtypeparameter jvmtypeparameter) {
        this.jvmtypeparameters.add(jvmtypeparameter);
    }

}
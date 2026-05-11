





import java.util.List;
import java.util.ArrayList;

public class model_ss_XtendEvent extends XtendMember {

    private String name;





    private JvmTypeReference jvmtypereference;




    private XExpression xexpression;


    public model_ss_XtendEvent(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public JvmTypeReference getJvmtypereference() {
        return jvmtypereference;
    }

    public void setJvmtypereference(JvmTypeReference jvmtypereference) {
        this.jvmtypereference = jvmtypereference;
    }
    public XExpression getXexpression() {
        return xexpression;
    }

    public void setXexpression(XExpression xexpression) {
        this.xexpression = xexpression;
    }

}
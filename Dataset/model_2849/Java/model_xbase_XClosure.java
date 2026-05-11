





import java.util.List;
import java.util.ArrayList;

public class model_xbase_XClosure extends xbase_XExpression, types_JvmIdentifiableElement {

    private boolean exported;
    private boolean operator;
    private String name;
    private boolean explicitSyntax;





    private XExpression xexpression;




    private JvmTypeReference jvmtypereference;




    private List<JvmFormalParameter> jvmformalparameters;




    private JvmFormalParameter jvmformalparameter;




    private List<JvmTypeParameter> jvmtypeparameters;


    public model_xbase_XClosure(
        boolean exported,        boolean operator,        String name,        boolean explicitSyntax    ) {
        super(
        );
        this.exported = exported;
        this.operator = operator;
        this.name = name;
        this.explicitSyntax = explicitSyntax;
        this.jvmformalparameters = new ArrayList<>();
        this.jvmtypeparameters = new ArrayList<>();
    }

    public model_xbase_XClosure(
        boolean exported,        boolean operator,        String name,        boolean explicitSyntax        ArrayList<JvmFormalParameter> jvmformalparameters,        ArrayList<JvmTypeParameter> jvmtypeparameters    ) {
        this.exported = exported;
        this.operator = operator;
        this.name = name;
        this.explicitSyntax = explicitSyntax;
        this.jvmformalparameters = jvmformalparameters;
        this.jvmtypeparameters = jvmtypeparameters;
    }

    public boolean getExported() {
        return exported;
    }

    public void setExported(boolean exported) {
        this.exported = exported;
    }
    public boolean getOperator() {
        return operator;
    }

    public void setOperator(boolean operator) {
        this.operator = operator;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getExplicitsyntax() {
        return explicitSyntax;
    }

    public void setExplicitsyntax(boolean explicitSyntax) {
        this.explicitSyntax = explicitSyntax;
    }

    public XExpression getXexpression() {
        return xexpression;
    }

    public void setXexpression(XExpression xexpression) {
        this.xexpression = xexpression;
    }
    public JvmTypeReference getJvmtypereference() {
        return jvmtypereference;
    }

    public void setJvmtypereference(JvmTypeReference jvmtypereference) {
        this.jvmtypereference = jvmtypereference;
    }
    public List<JvmFormalParameter> getJvmformalparameters() {
        return jvmformalparameters;
    }

    public void addJvmformalparameter(Jvmformalparameter jvmformalparameter) {
        this.jvmformalparameters.add(jvmformalparameter);
    }
    public JvmFormalParameter getJvmformalparameter() {
        return jvmformalparameter;
    }

    public void setJvmformalparameter(JvmFormalParameter jvmformalparameter) {
        this.jvmformalparameter = jvmformalparameter;
    }
    public List<JvmTypeParameter> getJvmtypeparameters() {
        return jvmtypeparameters;
    }

    public void addJvmtypeparameter(Jvmtypeparameter jvmtypeparameter) {
        this.jvmtypeparameters.add(jvmtypeparameter);
    }

}
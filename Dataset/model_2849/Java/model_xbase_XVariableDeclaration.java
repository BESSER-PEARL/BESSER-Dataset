





import java.util.List;
import java.util.ArrayList;

public class model_xbase_XVariableDeclaration extends xbase_XExpression, types_JvmIdentifiableElement {

    private boolean writeable;
    private String name;
    private boolean exported;





    private JvmTypeReference jvmtypereference;




    private XExpression xexpression;


    public model_xbase_XVariableDeclaration(
        boolean writeable,        String name,        boolean exported    ) {
        super(
        );
        this.writeable = writeable;
        this.name = name;
        this.exported = exported;
    }


    public boolean getWriteable() {
        return writeable;
    }

    public void setWriteable(boolean writeable) {
        this.writeable = writeable;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getExported() {
        return exported;
    }

    public void setExported(boolean exported) {
        this.exported = exported;
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
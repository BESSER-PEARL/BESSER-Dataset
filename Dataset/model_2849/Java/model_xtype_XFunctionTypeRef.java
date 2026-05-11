





import java.util.List;
import java.util.ArrayList;

public class model_xtype_XFunctionTypeRef extends JvmSpecializedTypeReference {

    private boolean instanceContext;





    private List<JvmTypeReference> jvmtypereferences;




    private JvmTypeReference jvmtypereference;




    private JvmType jvmtype;


    public model_xtype_XFunctionTypeRef(
        boolean instanceContext    ) {
        super(
        );
        this.instanceContext = instanceContext;
        this.jvmtypereferences = new ArrayList<>();
    }

    public model_xtype_XFunctionTypeRef(
        boolean instanceContext        ArrayList<JvmTypeReference> jvmtypereferences    ) {
        this.instanceContext = instanceContext;
        this.jvmtypereferences = jvmtypereferences;
    }

    public boolean getInstancecontext() {
        return instanceContext;
    }

    public void setInstancecontext(boolean instanceContext) {
        this.instanceContext = instanceContext;
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
    public JvmType getJvmtype() {
        return jvmtype;
    }

    public void setJvmtype(JvmType jvmtype) {
        this.jvmtype = jvmtype;
    }

}
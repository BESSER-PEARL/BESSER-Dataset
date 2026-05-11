





import java.util.List;
import java.util.ArrayList;

public class alf_QualifiedNameWithBinding  {

    private String id;





    private alf_TypeName alf_typename;




    private alf_QualifiedNameWithBinding alf_qualifiednamewithbinding;


    public alf_QualifiedNameWithBinding(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public alf_TypeName getAlf_typename() {
        return alf_typename;
    }

    public void setAlf_typename(alf_TypeName alf_typename) {
        this.alf_typename = alf_typename;
    }
    public alf_QualifiedNameWithBinding getAlf_qualifiednamewithbinding() {
        return alf_qualifiednamewithbinding;
    }

    public void setAlf_qualifiednamewithbinding(alf_QualifiedNameWithBinding alf_qualifiednamewithbinding) {
        this.alf_qualifiednamewithbinding = alf_qualifiednamewithbinding;
    }

}
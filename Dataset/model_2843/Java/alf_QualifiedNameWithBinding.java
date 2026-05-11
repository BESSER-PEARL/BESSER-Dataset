





import java.util.List;
import java.util.ArrayList;

public class alf_QualifiedNameWithBinding  {

    private String id;





    private alf_QualifiedNameWithBinding alf_qualifiednamewithbinding;




    private alf_NamedTemplateBinding alf_namedtemplatebinding;




    private alf_InstanceCreationExpression alf_instancecreationexpression;




    private alf_SuperInvocationExpression alf_superinvocationexpression;




    private alf_TemplateBinding alf_templatebinding;


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

    public alf_QualifiedNameWithBinding getAlf_qualifiednamewithbinding() {
        return alf_qualifiednamewithbinding;
    }

    public void setAlf_qualifiednamewithbinding(alf_QualifiedNameWithBinding alf_qualifiednamewithbinding) {
        this.alf_qualifiednamewithbinding = alf_qualifiednamewithbinding;
    }
    public alf_NamedTemplateBinding getAlf_namedtemplatebinding() {
        return alf_namedtemplatebinding;
    }

    public void setAlf_namedtemplatebinding(alf_NamedTemplateBinding alf_namedtemplatebinding) {
        this.alf_namedtemplatebinding = alf_namedtemplatebinding;
    }
    public alf_InstanceCreationExpression getAlf_instancecreationexpression() {
        return alf_instancecreationexpression;
    }

    public void setAlf_instancecreationexpression(alf_InstanceCreationExpression alf_instancecreationexpression) {
        this.alf_instancecreationexpression = alf_instancecreationexpression;
    }
    public alf_SuperInvocationExpression getAlf_superinvocationexpression() {
        return alf_superinvocationexpression;
    }

    public void setAlf_superinvocationexpression(alf_SuperInvocationExpression alf_superinvocationexpression) {
        this.alf_superinvocationexpression = alf_superinvocationexpression;
    }
    public alf_TemplateBinding getAlf_templatebinding() {
        return alf_templatebinding;
    }

    public void setAlf_templatebinding(alf_TemplateBinding alf_templatebinding) {
        this.alf_templatebinding = alf_templatebinding;
    }

}
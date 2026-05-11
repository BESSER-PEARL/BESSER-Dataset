





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedTemplateBinding extends TracedDirectedRelationship {






    private uml_TracedTemplateSignature uml_tracedtemplatesignature;




    private List<uml_TracedTemplateParameterSubstitution> uml_tracedtemplateparametersubstitutions;




    private uml_TracedTemplateableElement uml_tracedtemplateableelement;


    public umlTrace_uml_TracedTemplateBinding(
    ) {
        super(
        );
        this.uml_tracedtemplateparametersubstitutions = new ArrayList<>();
    }

    public umlTrace_uml_TracedTemplateBinding(
        ArrayList<uml_TracedTemplateParameterSubstitution> uml_tracedtemplateparametersubstitutions    ) {
        this.uml_tracedtemplateparametersubstitutions = uml_tracedtemplateparametersubstitutions;
    }


    public uml_TracedTemplateSignature getUml_tracedtemplatesignature() {
        return uml_tracedtemplatesignature;
    }

    public void setUml_tracedtemplatesignature(uml_TracedTemplateSignature uml_tracedtemplatesignature) {
        this.uml_tracedtemplatesignature = uml_tracedtemplatesignature;
    }
    public List<uml_TracedTemplateParameterSubstitution> getUml_tracedtemplateparametersubstitutions() {
        return uml_tracedtemplateparametersubstitutions;
    }

    public void addUml_tracedtemplateparametersubstitution(Uml_tracedtemplateparametersubstitution uml_tracedtemplateparametersubstitution) {
        this.uml_tracedtemplateparametersubstitutions.add(uml_tracedtemplateparametersubstitution);
    }
    public uml_TracedTemplateableElement getUml_tracedtemplateableelement() {
        return uml_tracedtemplateableelement;
    }

    public void setUml_tracedtemplateableelement(uml_TracedTemplateableElement uml_tracedtemplateableelement) {
        this.uml_tracedtemplateableelement = uml_tracedtemplateableelement;
    }

}
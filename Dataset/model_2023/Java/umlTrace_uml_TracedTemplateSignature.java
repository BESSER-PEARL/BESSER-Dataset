





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedTemplateSignature extends TracedElement {






    private uml_TracedTemplateableElement uml_tracedtemplateableelement;




    private List<uml_TracedTemplateParameter> uml_tracedtemplateparameters;




    private List<uml_TracedTemplateParameter> uml_tracedtemplateparameters;


    public umlTrace_uml_TracedTemplateSignature(
    ) {
        super(
        );
        this.uml_tracedtemplateparameters = new ArrayList<>();
        this.uml_tracedtemplateparameters = new ArrayList<>();
    }

    public umlTrace_uml_TracedTemplateSignature(
        ArrayList<uml_TracedTemplateParameter> uml_tracedtemplateparameters,        ArrayList<uml_TracedTemplateParameter> uml_tracedtemplateparameters    ) {
        this.uml_tracedtemplateparameters = uml_tracedtemplateparameters;
        this.uml_tracedtemplateparameters = uml_tracedtemplateparameters;
    }


    public uml_TracedTemplateableElement getUml_tracedtemplateableelement() {
        return uml_tracedtemplateableelement;
    }

    public void setUml_tracedtemplateableelement(uml_TracedTemplateableElement uml_tracedtemplateableelement) {
        this.uml_tracedtemplateableelement = uml_tracedtemplateableelement;
    }
    public List<uml_TracedTemplateParameter> getUml_tracedtemplateparameters() {
        return uml_tracedtemplateparameters;
    }

    public void addUml_tracedtemplateparameter(Uml_tracedtemplateparameter uml_tracedtemplateparameter) {
        this.uml_tracedtemplateparameters.add(uml_tracedtemplateparameter);
    }
    public List<uml_TracedTemplateParameter> getUml_tracedtemplateparameters() {
        return uml_tracedtemplateparameters;
    }

    public void addUml_tracedtemplateparameter(Uml_tracedtemplateparameter uml_tracedtemplateparameter) {
        this.uml_tracedtemplateparameters.add(uml_tracedtemplateparameter);
    }

}






import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedTemplateableElement extends TracedElement {






    private uml_TracedTemplateSignature uml_tracedtemplatesignature;




    private List<uml_TracedTemplateBinding> uml_tracedtemplatebindings;


    public umlTrace_uml_TracedTemplateableElement(
    ) {
        super(
        );
        this.uml_tracedtemplatebindings = new ArrayList<>();
    }

    public umlTrace_uml_TracedTemplateableElement(
        ArrayList<uml_TracedTemplateBinding> uml_tracedtemplatebindings    ) {
        this.uml_tracedtemplatebindings = uml_tracedtemplatebindings;
    }


    public uml_TracedTemplateSignature getUml_tracedtemplatesignature() {
        return uml_tracedtemplatesignature;
    }

    public void setUml_tracedtemplatesignature(uml_TracedTemplateSignature uml_tracedtemplatesignature) {
        this.uml_tracedtemplatesignature = uml_tracedtemplatesignature;
    }
    public List<uml_TracedTemplateBinding> getUml_tracedtemplatebindings() {
        return uml_tracedtemplatebindings;
    }

    public void addUml_tracedtemplatebinding(Uml_tracedtemplatebinding uml_tracedtemplatebinding) {
        this.uml_tracedtemplatebindings.add(uml_tracedtemplatebinding);
    }

}






import java.util.List;
import java.util.ArrayList;

public class UML2_TemplateableElement extends Element {






    private UML2_TemplateBinding uml2_templatebinding;




    private UML2_TemplateSignature uml2_templatesignature;




    private List<UML2_TemplateBinding> uml2_templatebindings;




    private UML2_TemplateSignature uml2_templatesignature;


    public UML2_TemplateableElement(
    ) {
        super(
        );
        this.uml2_templatebindings = new ArrayList<>();
    }

    public UML2_TemplateableElement(
        ArrayList<UML2_TemplateBinding> uml2_templatebindings    ) {
        this.uml2_templatebindings = uml2_templatebindings;
    }


    public UML2_TemplateBinding getUml2_templatebinding() {
        return uml2_templatebinding;
    }

    public void setUml2_templatebinding(UML2_TemplateBinding uml2_templatebinding) {
        this.uml2_templatebinding = uml2_templatebinding;
    }
    public UML2_TemplateSignature getUml2_templatesignature() {
        return uml2_templatesignature;
    }

    public void setUml2_templatesignature(UML2_TemplateSignature uml2_templatesignature) {
        this.uml2_templatesignature = uml2_templatesignature;
    }
    public List<UML2_TemplateBinding> getUml2_templatebindings() {
        return uml2_templatebindings;
    }

    public void addUml2_templatebinding(Uml2_templatebinding uml2_templatebinding) {
        this.uml2_templatebindings.add(uml2_templatebinding);
    }
    public UML2_TemplateSignature getUml2_templatesignature() {
        return uml2_templatesignature;
    }

    public void setUml2_templatesignature(UML2_TemplateSignature uml2_templatesignature) {
        this.uml2_templatesignature = uml2_templatesignature;
    }

}
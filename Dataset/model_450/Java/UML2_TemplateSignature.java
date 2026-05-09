





import java.util.List;
import java.util.ArrayList;

public class UML2_TemplateSignature extends Element {






    private List<UML2_TemplateSignature> uml2_templatesignatures;




    private UML2_TemplateSignature uml2_templatesignature;




    private UML2_TemplateBinding uml2_templatebinding;


    public UML2_TemplateSignature(
    ) {
        super(
        );
        this.uml2_templatesignatures = new ArrayList<>();
    }

    public UML2_TemplateSignature(
        ArrayList<UML2_TemplateSignature> uml2_templatesignatures    ) {
        this.uml2_templatesignatures = uml2_templatesignatures;
    }


    public List<UML2_TemplateSignature> getUml2_templatesignatures() {
        return uml2_templatesignatures;
    }

    public void addUml2_templatesignature(Uml2_templatesignature uml2_templatesignature) {
        this.uml2_templatesignatures.add(uml2_templatesignature);
    }
    public UML2_TemplateSignature getUml2_templatesignature() {
        return uml2_templatesignature;
    }

    public void setUml2_templatesignature(UML2_TemplateSignature uml2_templatesignature) {
        this.uml2_templatesignature = uml2_templatesignature;
    }
    public UML2_TemplateBinding getUml2_templatebinding() {
        return uml2_templatebinding;
    }

    public void setUml2_templatebinding(UML2_TemplateBinding uml2_templatebinding) {
        this.uml2_templatebinding = uml2_templatebinding;
    }

}
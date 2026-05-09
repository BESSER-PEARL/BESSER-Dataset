





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_TemplateableElement extends Element {






    private UML2WithID_TemplateBinding uml2withid_templatebinding;




    private List<UML2WithID_TemplateBinding> uml2withid_templatebindings;


    public UML2WithID_TemplateableElement(
    ) {
        super(
        );
        this.uml2withid_templatebindings = new ArrayList<>();
    }

    public UML2WithID_TemplateableElement(
        ArrayList<UML2WithID_TemplateBinding> uml2withid_templatebindings    ) {
        this.uml2withid_templatebindings = uml2withid_templatebindings;
    }


    public UML2WithID_TemplateBinding getUml2withid_templatebinding() {
        return uml2withid_templatebinding;
    }

    public void setUml2withid_templatebinding(UML2WithID_TemplateBinding uml2withid_templatebinding) {
        this.uml2withid_templatebinding = uml2withid_templatebinding;
    }
    public List<UML2WithID_TemplateBinding> getUml2withid_templatebindings() {
        return uml2withid_templatebindings;
    }

    public void addUml2withid_templatebinding(Uml2withid_templatebinding uml2withid_templatebinding) {
        this.uml2withid_templatebindings.add(uml2withid_templatebinding);
    }

}
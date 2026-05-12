





import java.util.List;
import java.util.ArrayList;

public class pivot_TemplateableElement extends Element {






    private pivot_TemplateSignature pivot_templatesignature;




    private List<pivot_TemplateBinding> pivot_templatebindings;




    private pivot_TemplateSignature pivot_templatesignature;




    private pivot_TemplateableElement pivot_templateableelement;




    private pivot_TemplateBinding pivot_templatebinding;


    public pivot_TemplateableElement(
    ) {
        super(
        );
        this.pivot_templatebindings = new ArrayList<>();
    }

    public pivot_TemplateableElement(
        ArrayList<pivot_TemplateBinding> pivot_templatebindings    ) {
        this.pivot_templatebindings = pivot_templatebindings;
    }


    public pivot_TemplateSignature getPivot_templatesignature() {
        return pivot_templatesignature;
    }

    public void setPivot_templatesignature(pivot_TemplateSignature pivot_templatesignature) {
        this.pivot_templatesignature = pivot_templatesignature;
    }
    public List<pivot_TemplateBinding> getPivot_templatebindings() {
        return pivot_templatebindings;
    }

    public void addPivot_templatebinding(Pivot_templatebinding pivot_templatebinding) {
        this.pivot_templatebindings.add(pivot_templatebinding);
    }
    public pivot_TemplateSignature getPivot_templatesignature() {
        return pivot_templatesignature;
    }

    public void setPivot_templatesignature(pivot_TemplateSignature pivot_templatesignature) {
        this.pivot_templatesignature = pivot_templatesignature;
    }
    public pivot_TemplateableElement getPivot_templateableelement() {
        return pivot_templateableelement;
    }

    public void setPivot_templateableelement(pivot_TemplateableElement pivot_templateableelement) {
        this.pivot_templateableelement = pivot_templateableelement;
    }
    public pivot_TemplateBinding getPivot_templatebinding() {
        return pivot_templatebinding;
    }

    public void setPivot_templatebinding(pivot_TemplateBinding pivot_templatebinding) {
        this.pivot_templatebinding = pivot_templatebinding;
    }

}
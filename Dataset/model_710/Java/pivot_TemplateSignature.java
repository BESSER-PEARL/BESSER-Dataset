





import java.util.List;
import java.util.ArrayList;

public class pivot_TemplateSignature extends Element {






    private List<pivot_TemplateParameter> pivot_templateparameters;




    private List<pivot_TemplateParameter> pivot_templateparameters;




    private pivot_TemplateBinding pivot_templatebinding;




    private pivot_TemplateParameter pivot_templateparameter;


    public pivot_TemplateSignature(
    ) {
        super(
        );
        this.pivot_templateparameters = new ArrayList<>();
        this.pivot_templateparameters = new ArrayList<>();
    }

    public pivot_TemplateSignature(
        ArrayList<pivot_TemplateParameter> pivot_templateparameters,        ArrayList<pivot_TemplateParameter> pivot_templateparameters    ) {
        this.pivot_templateparameters = pivot_templateparameters;
        this.pivot_templateparameters = pivot_templateparameters;
    }


    public List<pivot_TemplateParameter> getPivot_templateparameters() {
        return pivot_templateparameters;
    }

    public void addPivot_templateparameter(Pivot_templateparameter pivot_templateparameter) {
        this.pivot_templateparameters.add(pivot_templateparameter);
    }
    public List<pivot_TemplateParameter> getPivot_templateparameters() {
        return pivot_templateparameters;
    }

    public void addPivot_templateparameter(Pivot_templateparameter pivot_templateparameter) {
        this.pivot_templateparameters.add(pivot_templateparameter);
    }
    public pivot_TemplateBinding getPivot_templatebinding() {
        return pivot_templatebinding;
    }

    public void setPivot_templatebinding(pivot_TemplateBinding pivot_templatebinding) {
        this.pivot_templatebinding = pivot_templatebinding;
    }
    public pivot_TemplateParameter getPivot_templateparameter() {
        return pivot_templateparameter;
    }

    public void setPivot_templateparameter(pivot_TemplateParameter pivot_templateparameter) {
        this.pivot_templateparameter = pivot_templateparameter;
    }

}
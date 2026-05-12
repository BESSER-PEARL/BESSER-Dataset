





import java.util.List;
import java.util.ArrayList;

public class sparqlas_TemplateSignature  {






    private sparqlas_TemplateParameter sparqlas_templateparameter;




    private List<sparqlas_TemplateParameter> sparqlas_templateparameters;


    public sparqlas_TemplateSignature(
    ) {
        this.sparqlas_templateparameters = new ArrayList<>();
    }

    public sparqlas_TemplateSignature(
        ArrayList<sparqlas_TemplateParameter> sparqlas_templateparameters    ) {
        this.sparqlas_templateparameters = sparqlas_templateparameters;
    }


    public sparqlas_TemplateParameter getSparqlas_templateparameter() {
        return sparqlas_templateparameter;
    }

    public void setSparqlas_templateparameter(sparqlas_TemplateParameter sparqlas_templateparameter) {
        this.sparqlas_templateparameter = sparqlas_templateparameter;
    }
    public List<sparqlas_TemplateParameter> getSparqlas_templateparameters() {
        return sparqlas_templateparameters;
    }

    public void addSparqlas_templateparameter(Sparqlas_templateparameter sparqlas_templateparameter) {
        this.sparqlas_templateparameters.add(sparqlas_templateparameter);
    }

}
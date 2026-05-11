





import java.util.List;
import java.util.ArrayList;

public class KM3_Class extends Classifier {

    private String isAbstract;





    private KM3_Class km3_class;




    private List<KM3_TemplateParameter> km3_templateparameters;


    public KM3_Class(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.km3_templateparameters = new ArrayList<>();
    }

    public KM3_Class(
        String isAbstract        ArrayList<KM3_TemplateParameter> km3_templateparameters    ) {
        this.isAbstract = isAbstract;
        this.km3_templateparameters = km3_templateparameters;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public KM3_Class getKm3_class() {
        return km3_class;
    }

    public void setKm3_class(KM3_Class km3_class) {
        this.km3_class = km3_class;
    }
    public List<KM3_TemplateParameter> getKm3_templateparameters() {
        return km3_templateparameters;
    }

    public void addKm3_templateparameter(Km3_templateparameter km3_templateparameter) {
        this.km3_templateparameters.add(km3_templateparameter);
    }

}
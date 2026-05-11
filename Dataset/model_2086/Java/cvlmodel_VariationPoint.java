





import java.util.List;
import java.util.ArrayList;

public class cvlmodel_VariationPoint  {

    private String modelTransformationSourceURL;
    private String name;
    private String negativeVariability;
    private String modelTransformationURL;





    private cvlmodel_VSpec cvlmodel_vspec;


    public cvlmodel_VariationPoint(
        String modelTransformationSourceURL,        String name,        String negativeVariability,        String modelTransformationURL    ) {
        this.modelTransformationSourceURL = modelTransformationSourceURL;
        this.name = name;
        this.negativeVariability = negativeVariability;
        this.modelTransformationURL = modelTransformationURL;
    }


    public String getModeltransformationsourceurl() {
        return modelTransformationSourceURL;
    }

    public void setModeltransformationsourceurl(String modelTransformationSourceURL) {
        this.modelTransformationSourceURL = modelTransformationSourceURL;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNegativevariability() {
        return negativeVariability;
    }

    public void setNegativevariability(String negativeVariability) {
        this.negativeVariability = negativeVariability;
    }
    public String getModeltransformationurl() {
        return modelTransformationURL;
    }

    public void setModeltransformationurl(String modelTransformationURL) {
        this.modelTransformationURL = modelTransformationURL;
    }

    public cvlmodel_VSpec getCvlmodel_vspec() {
        return cvlmodel_vspec;
    }

    public void setCvlmodel_vspec(cvlmodel_VSpec cvlmodel_vspec) {
        this.cvlmodel_vspec = cvlmodel_vspec;
    }

}
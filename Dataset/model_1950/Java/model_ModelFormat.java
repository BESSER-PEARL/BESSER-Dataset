





import java.util.List;
import java.util.ArrayList;

public class model_ModelFormat  {

    private String modelFormat;





    private model_DomainModel model_domainmodel;


    public model_ModelFormat(
        String modelFormat    ) {
        this.modelFormat = modelFormat;
    }


    public String getModelformat() {
        return modelFormat;
    }

    public void setModelformat(String modelFormat) {
        this.modelFormat = modelFormat;
    }

    public model_DomainModel getModel_domainmodel() {
        return model_domainmodel;
    }

    public void setModel_domainmodel(model_DomainModel model_domainmodel) {
        this.model_domainmodel = model_domainmodel;
    }

}
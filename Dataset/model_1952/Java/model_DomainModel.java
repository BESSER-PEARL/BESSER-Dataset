





import java.util.List;
import java.util.ArrayList;

public class model_DomainModel  {

    private String domainModel;





    private model_ModelFormat model_modelformat;


    public model_DomainModel(
        String domainModel    ) {
        this.domainModel = domainModel;
    }


    public String getDomainmodel() {
        return domainModel;
    }

    public void setDomainmodel(String domainModel) {
        this.domainModel = domainModel;
    }

    public model_ModelFormat getModel_modelformat() {
        return model_modelformat;
    }

    public void setModel_modelformat(model_ModelFormat model_modelformat) {
        this.model_modelformat = model_modelformat;
    }

}
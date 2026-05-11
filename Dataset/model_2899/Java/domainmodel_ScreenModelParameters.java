





import java.util.List;
import java.util.ArrayList;

public class domainmodel_ScreenModelParameters  {






    private List<domainmodel_ScreenModelParameter> domainmodel_screenmodelparameters;


    public domainmodel_ScreenModelParameters(
    ) {
        this.domainmodel_screenmodelparameters = new ArrayList<>();
    }

    public domainmodel_ScreenModelParameters(
        ArrayList<domainmodel_ScreenModelParameter> domainmodel_screenmodelparameters    ) {
        this.domainmodel_screenmodelparameters = domainmodel_screenmodelparameters;
    }


    public List<domainmodel_ScreenModelParameter> getDomainmodel_screenmodelparameters() {
        return domainmodel_screenmodelparameters;
    }

    public void addDomainmodel_screenmodelparameter(Domainmodel_screenmodelparameter domainmodel_screenmodelparameter) {
        this.domainmodel_screenmodelparameters.add(domainmodel_screenmodelparameter);
    }

}
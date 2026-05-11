





import java.util.List;
import java.util.ArrayList;

public class domainmodel_MethodParameters  {






    private List<domainmodel_MethodParameter> domainmodel_methodparameters;


    public domainmodel_MethodParameters(
    ) {
        this.domainmodel_methodparameters = new ArrayList<>();
    }

    public domainmodel_MethodParameters(
        ArrayList<domainmodel_MethodParameter> domainmodel_methodparameters    ) {
        this.domainmodel_methodparameters = domainmodel_methodparameters;
    }


    public List<domainmodel_MethodParameter> getDomainmodel_methodparameters() {
        return domainmodel_methodparameters;
    }

    public void addDomainmodel_methodparameter(Domainmodel_methodparameter domainmodel_methodparameter) {
        this.domainmodel_methodparameters.add(domainmodel_methodparameter);
    }

}
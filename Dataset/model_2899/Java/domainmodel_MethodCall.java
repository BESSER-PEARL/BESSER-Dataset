





import java.util.List;
import java.util.ArrayList;

public class domainmodel_MethodCall  {

    private String name;





    private domainmodel_MethodParameters domainmodel_methodparameters;


    public domainmodel_MethodCall(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public domainmodel_MethodParameters getDomainmodel_methodparameters() {
        return domainmodel_methodparameters;
    }

    public void setDomainmodel_methodparameters(domainmodel_MethodParameters domainmodel_methodparameters) {
        this.domainmodel_methodparameters = domainmodel_methodparameters;
    }

}
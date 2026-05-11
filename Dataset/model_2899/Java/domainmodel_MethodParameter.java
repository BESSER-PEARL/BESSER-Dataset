





import java.util.List;
import java.util.ArrayList;

public class domainmodel_MethodParameter  {

    private String name;





    private domainmodel_Type domainmodel_type;


    public domainmodel_MethodParameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public domainmodel_Type getDomainmodel_type() {
        return domainmodel_type;
    }

    public void setDomainmodel_type(domainmodel_Type domainmodel_type) {
        this.domainmodel_type = domainmodel_type;
    }

}






import java.util.List;
import java.util.ArrayList;

public class types_Domain  {

    private String domainID;





    private types_Package types_package;


    public types_Domain(
        String domainID    ) {
        this.domainID = domainID;
    }


    public String getDomainid() {
        return domainID;
    }

    public void setDomainid(String domainID) {
        this.domainID = domainID;
    }

    public types_Package getTypes_package() {
        return types_package;
    }

    public void setTypes_package(types_Package types_package) {
        this.types_package = types_package;
    }

}
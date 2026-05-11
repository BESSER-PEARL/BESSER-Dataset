





import java.util.List;
import java.util.ArrayList;

public class domainmodel_DomainRepository extends BusinessFeatureType, AbstractNamespaceElement {

    private String name;





    private domainmodel_DomainEntity domainmodel_domainentity;


    public domainmodel_DomainRepository(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public domainmodel_DomainEntity getDomainmodel_domainentity() {
        return domainmodel_domainentity;
    }

    public void setDomainmodel_domainentity(domainmodel_DomainEntity domainmodel_domainentity) {
        this.domainmodel_domainentity = domainmodel_domainentity;
    }

}
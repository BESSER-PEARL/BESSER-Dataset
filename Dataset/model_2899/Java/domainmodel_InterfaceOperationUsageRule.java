





import java.util.List;
import java.util.ArrayList;

public class domainmodel_InterfaceOperationUsageRule  {

    private String name;





    private domainmodel_InterfaceDeclaration domainmodel_interfacedeclaration;




    private domainmodel_InterfaceOperationsUsageRule domainmodel_interfaceoperationsusagerule;


    public domainmodel_InterfaceOperationUsageRule(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public domainmodel_InterfaceDeclaration getDomainmodel_interfacedeclaration() {
        return domainmodel_interfacedeclaration;
    }

    public void setDomainmodel_interfacedeclaration(domainmodel_InterfaceDeclaration domainmodel_interfacedeclaration) {
        this.domainmodel_interfacedeclaration = domainmodel_interfacedeclaration;
    }
    public domainmodel_InterfaceOperationsUsageRule getDomainmodel_interfaceoperationsusagerule() {
        return domainmodel_interfaceoperationsusagerule;
    }

    public void setDomainmodel_interfaceoperationsusagerule(domainmodel_InterfaceOperationsUsageRule domainmodel_interfaceoperationsusagerule) {
        this.domainmodel_interfaceoperationsusagerule = domainmodel_interfaceoperationsusagerule;
    }

}
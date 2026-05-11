





import java.util.List;
import java.util.ArrayList;

public class domainmodel_InterfaceOperation  {

    private String restOperation;





    private domainmodel_Type domainmodel_type;




    private domainmodel_MethodCall domainmodel_methodcall;




    private domainmodel_InterfaceDeclaration domainmodel_interfacedeclaration;


    public domainmodel_InterfaceOperation(
        String restOperation    ) {
        this.restOperation = restOperation;
    }


    public String getRestoperation() {
        return restOperation;
    }

    public void setRestoperation(String restOperation) {
        this.restOperation = restOperation;
    }

    public domainmodel_Type getDomainmodel_type() {
        return domainmodel_type;
    }

    public void setDomainmodel_type(domainmodel_Type domainmodel_type) {
        this.domainmodel_type = domainmodel_type;
    }
    public domainmodel_MethodCall getDomainmodel_methodcall() {
        return domainmodel_methodcall;
    }

    public void setDomainmodel_methodcall(domainmodel_MethodCall domainmodel_methodcall) {
        this.domainmodel_methodcall = domainmodel_methodcall;
    }
    public domainmodel_InterfaceDeclaration getDomainmodel_interfacedeclaration() {
        return domainmodel_interfacedeclaration;
    }

    public void setDomainmodel_interfacedeclaration(domainmodel_InterfaceDeclaration domainmodel_interfacedeclaration) {
        this.domainmodel_interfacedeclaration = domainmodel_interfacedeclaration;
    }

}






import java.util.List;
import java.util.ArrayList;

public class domainmodel_Parameter  {

    private String name;





    private domainmodel_Operation domainmodel_operation;




    private domainmodel_TypeRef domainmodel_typeref;


    public domainmodel_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public domainmodel_Operation getDomainmodel_operation() {
        return domainmodel_operation;
    }

    public void setDomainmodel_operation(domainmodel_Operation domainmodel_operation) {
        this.domainmodel_operation = domainmodel_operation;
    }
    public domainmodel_TypeRef getDomainmodel_typeref() {
        return domainmodel_typeref;
    }

    public void setDomainmodel_typeref(domainmodel_TypeRef domainmodel_typeref) {
        this.domainmodel_typeref = domainmodel_typeref;
    }

}
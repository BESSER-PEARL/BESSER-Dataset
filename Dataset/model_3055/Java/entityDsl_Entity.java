





import java.util.List;
import java.util.ArrayList;

public class entityDsl_Entity  {

    private String name;





    private entityDsl_Domainmodel entitydsl_domainmodel;


    public entityDsl_Entity(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public entityDsl_Domainmodel getEntitydsl_domainmodel() {
        return entitydsl_domainmodel;
    }

    public void setEntitydsl_domainmodel(entityDsl_Domainmodel entitydsl_domainmodel) {
        this.entitydsl_domainmodel = entitydsl_domainmodel;
    }

}
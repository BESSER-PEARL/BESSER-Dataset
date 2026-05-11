





import java.util.List;
import java.util.ArrayList;

public class domainmodel_ModelFeature  {

    private String name;





    private domainmodel_EntryParametersModule domainmodel_entryparametersmodule;




    private domainmodel_ModelModule domainmodel_modelmodule;




    private domainmodel_Type domainmodel_type;


    public domainmodel_ModelFeature(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public domainmodel_EntryParametersModule getDomainmodel_entryparametersmodule() {
        return domainmodel_entryparametersmodule;
    }

    public void setDomainmodel_entryparametersmodule(domainmodel_EntryParametersModule domainmodel_entryparametersmodule) {
        this.domainmodel_entryparametersmodule = domainmodel_entryparametersmodule;
    }
    public domainmodel_ModelModule getDomainmodel_modelmodule() {
        return domainmodel_modelmodule;
    }

    public void setDomainmodel_modelmodule(domainmodel_ModelModule domainmodel_modelmodule) {
        this.domainmodel_modelmodule = domainmodel_modelmodule;
    }
    public domainmodel_Type getDomainmodel_type() {
        return domainmodel_type;
    }

    public void setDomainmodel_type(domainmodel_Type domainmodel_type) {
        this.domainmodel_type = domainmodel_type;
    }

}
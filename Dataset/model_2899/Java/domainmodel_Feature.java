





import java.util.List;
import java.util.ArrayList;

public class domainmodel_Feature  {

    private String name;
    private String mappingOption;
    private String mapName;





    private domainmodel_Type domainmodel_type;




    private domainmodel_DomainEntity domainmodel_domainentity;


    public domainmodel_Feature(
        String name,        String mappingOption,        String mapName    ) {
        this.name = name;
        this.mappingOption = mappingOption;
        this.mapName = mapName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMappingoption() {
        return mappingOption;
    }

    public void setMappingoption(String mappingOption) {
        this.mappingOption = mappingOption;
    }
    public String getMapname() {
        return mapName;
    }

    public void setMapname(String mapName) {
        this.mapName = mapName;
    }

    public domainmodel_Type getDomainmodel_type() {
        return domainmodel_type;
    }

    public void setDomainmodel_type(domainmodel_Type domainmodel_type) {
        this.domainmodel_type = domainmodel_type;
    }
    public domainmodel_DomainEntity getDomainmodel_domainentity() {
        return domainmodel_domainentity;
    }

    public void setDomainmodel_domainentity(domainmodel_DomainEntity domainmodel_domainentity) {
        this.domainmodel_domainentity = domainmodel_domainentity;
    }

}
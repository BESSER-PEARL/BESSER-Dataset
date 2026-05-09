





import java.util.List;
import java.util.ArrayList;

public class eTJ_Extend  {

    private boolean inherit;
    private boolean scenariospecific;
    private String name;
    private String description;





    private eTJ_ExtendedResourceAttribute etj_extendedresourceattribute;




    private eTJ_ExtendedResourceAttributeColumn etj_extendedresourceattributecolumn;




    private eTJ_ExtendResource etj_extendresource;




    private eTJ_ExtendTask etj_extendtask;


    public eTJ_Extend(
        boolean inherit,        boolean scenariospecific,        String name,        String description    ) {
        this.inherit = inherit;
        this.scenariospecific = scenariospecific;
        this.name = name;
        this.description = description;
    }


    public boolean getInherit() {
        return inherit;
    }

    public void setInherit(boolean inherit) {
        this.inherit = inherit;
    }
    public boolean getScenariospecific() {
        return scenariospecific;
    }

    public void setScenariospecific(boolean scenariospecific) {
        this.scenariospecific = scenariospecific;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public eTJ_ExtendedResourceAttribute getEtj_extendedresourceattribute() {
        return etj_extendedresourceattribute;
    }

    public void setEtj_extendedresourceattribute(eTJ_ExtendedResourceAttribute etj_extendedresourceattribute) {
        this.etj_extendedresourceattribute = etj_extendedresourceattribute;
    }
    public eTJ_ExtendedResourceAttributeColumn getEtj_extendedresourceattributecolumn() {
        return etj_extendedresourceattributecolumn;
    }

    public void setEtj_extendedresourceattributecolumn(eTJ_ExtendedResourceAttributeColumn etj_extendedresourceattributecolumn) {
        this.etj_extendedresourceattributecolumn = etj_extendedresourceattributecolumn;
    }
    public eTJ_ExtendResource getEtj_extendresource() {
        return etj_extendresource;
    }

    public void setEtj_extendresource(eTJ_ExtendResource etj_extendresource) {
        this.etj_extendresource = etj_extendresource;
    }
    public eTJ_ExtendTask getEtj_extendtask() {
        return etj_extendtask;
    }

    public void setEtj_extendtask(eTJ_ExtendTask etj_extendtask) {
        this.etj_extendtask = etj_extendtask;
    }

}
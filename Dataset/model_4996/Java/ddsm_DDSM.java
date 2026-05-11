





import java.util.List;
import java.util.ArrayList;

public class ddsm_DDSM  {

    private String description;
    private String modelId;





    private List<ddsm_Resource> ddsm_resources;




    private List<ddsm_CloudElement> ddsm_cloudelements;




    private List<ddsm_Property> ddsm_propertys;


    public ddsm_DDSM(
        String description,        String modelId    ) {
        this.description = description;
        this.modelId = modelId;
        this.ddsm_resources = new ArrayList<>();
        this.ddsm_cloudelements = new ArrayList<>();
        this.ddsm_propertys = new ArrayList<>();
    }

    public ddsm_DDSM(
        String description,        String modelId        ArrayList<ddsm_Resource> ddsm_resources,        ArrayList<ddsm_CloudElement> ddsm_cloudelements,        ArrayList<ddsm_Property> ddsm_propertys    ) {
        this.description = description;
        this.modelId = modelId;
        this.ddsm_resources = ddsm_resources;
        this.ddsm_cloudelements = ddsm_cloudelements;
        this.ddsm_propertys = ddsm_propertys;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getModelid() {
        return modelId;
    }

    public void setModelid(String modelId) {
        this.modelId = modelId;
    }

    public List<ddsm_Resource> getDdsm_resources() {
        return ddsm_resources;
    }

    public void addDdsm_resource(Ddsm_resource ddsm_resource) {
        this.ddsm_resources.add(ddsm_resource);
    }
    public List<ddsm_CloudElement> getDdsm_cloudelements() {
        return ddsm_cloudelements;
    }

    public void addDdsm_cloudelement(Ddsm_cloudelement ddsm_cloudelement) {
        this.ddsm_cloudelements.add(ddsm_cloudelement);
    }
    public List<ddsm_Property> getDdsm_propertys() {
        return ddsm_propertys;
    }

    public void addDdsm_property(Ddsm_property ddsm_property) {
        this.ddsm_propertys.add(ddsm_property);
    }

}
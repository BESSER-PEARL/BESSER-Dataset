





import java.util.List;
import java.util.ArrayList;

public class ddsm_DDSM  {

    private String modelId;
    private String description;





    private List<ddsm_Artifact> ddsm_artifacts;




    private List<ddsm_Property> ddsm_propertys;




    private List<ddsm_Resource> ddsm_resources;




    private List<ddsm_CloudElement> ddsm_cloudelements;


    public ddsm_DDSM(
        String modelId,        String description    ) {
        this.modelId = modelId;
        this.description = description;
        this.ddsm_artifacts = new ArrayList<>();
        this.ddsm_propertys = new ArrayList<>();
        this.ddsm_resources = new ArrayList<>();
        this.ddsm_cloudelements = new ArrayList<>();
    }

    public ddsm_DDSM(
        String modelId,        String description        ArrayList<ddsm_Artifact> ddsm_artifacts,        ArrayList<ddsm_Property> ddsm_propertys,        ArrayList<ddsm_Resource> ddsm_resources,        ArrayList<ddsm_CloudElement> ddsm_cloudelements    ) {
        this.modelId = modelId;
        this.description = description;
        this.ddsm_artifacts = ddsm_artifacts;
        this.ddsm_propertys = ddsm_propertys;
        this.ddsm_resources = ddsm_resources;
        this.ddsm_cloudelements = ddsm_cloudelements;
    }

    public String getModelid() {
        return modelId;
    }

    public void setModelid(String modelId) {
        this.modelId = modelId;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<ddsm_Artifact> getDdsm_artifacts() {
        return ddsm_artifacts;
    }

    public void addDdsm_artifact(Ddsm_artifact ddsm_artifact) {
        this.ddsm_artifacts.add(ddsm_artifact);
    }
    public List<ddsm_Property> getDdsm_propertys() {
        return ddsm_propertys;
    }

    public void addDdsm_property(Ddsm_property ddsm_property) {
        this.ddsm_propertys.add(ddsm_property);
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

}
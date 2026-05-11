





import java.util.List;
import java.util.ArrayList;

public class model_ModelObject  {

    private String name;
    private String uniqueName;
    private String description;
    private String id;





    private List<model_ModelPropertyMapEntry> model_modelpropertymapentrys;


    public model_ModelObject(
        String name,        String uniqueName,        String description,        String id    ) {
        this.name = name;
        this.uniqueName = uniqueName;
        this.description = description;
        this.id = id;
        this.model_modelpropertymapentrys = new ArrayList<>();
    }

    public model_ModelObject(
        String name,        String uniqueName,        String description,        String id        ArrayList<model_ModelPropertyMapEntry> model_modelpropertymapentrys    ) {
        this.name = name;
        this.uniqueName = uniqueName;
        this.description = description;
        this.id = id;
        this.model_modelpropertymapentrys = model_modelpropertymapentrys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUniquename() {
        return uniqueName;
    }

    public void setUniquename(String uniqueName) {
        this.uniqueName = uniqueName;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<model_ModelPropertyMapEntry> getModel_modelpropertymapentrys() {
        return model_modelpropertymapentrys;
    }

    public void addModel_modelpropertymapentry(Model_modelpropertymapentry model_modelpropertymapentry) {
        this.model_modelpropertymapentrys.add(model_modelpropertymapentry);
    }

}
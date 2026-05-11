





import java.util.List;
import java.util.ArrayList;

public class model_TopicMapSchema extends TMCLConstruct {

    private String schemaResource;
    private String includes;
    private String name;
    private String baseLocator;
    private String version;





    private List<model_TopicType> model_topictypes;


    public model_TopicMapSchema(
        String schemaResource,        String includes,        String name,        String baseLocator,        String version    ) {
        super(
        );
        this.schemaResource = schemaResource;
        this.includes = includes;
        this.name = name;
        this.baseLocator = baseLocator;
        this.version = version;
        this.model_topictypes = new ArrayList<>();
    }

    public model_TopicMapSchema(
        String schemaResource,        String includes,        String name,        String baseLocator,        String version        ArrayList<model_TopicType> model_topictypes    ) {
        this.schemaResource = schemaResource;
        this.includes = includes;
        this.name = name;
        this.baseLocator = baseLocator;
        this.version = version;
        this.model_topictypes = model_topictypes;
    }

    public String getSchemaresource() {
        return schemaResource;
    }

    public void setSchemaresource(String schemaResource) {
        this.schemaResource = schemaResource;
    }
    public String getIncludes() {
        return includes;
    }

    public void setIncludes(String includes) {
        this.includes = includes;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBaselocator() {
        return baseLocator;
    }

    public void setBaselocator(String baseLocator) {
        this.baseLocator = baseLocator;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public List<model_TopicType> getModel_topictypes() {
        return model_topictypes;
    }

    public void addModel_topictype(Model_topictype model_topictype) {
        this.model_topictypes.add(model_topictype);
    }

}
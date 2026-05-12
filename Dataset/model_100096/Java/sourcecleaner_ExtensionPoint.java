





import java.util.List;
import java.util.ArrayList;

public class sourcecleaner_ExtensionPoint  {

    private String name;
    private String schema;
    private boolean diagraph;
    private String id;





    private sourcecleaner_Plugin sourcecleaner_plugin;




    private sourcecleaner_Plugin sourcecleaner_plugin;




    private sourcecleaner_Extension sourcecleaner_extension;




    private List<sourcecleaner_Extension> sourcecleaner_extensions;


    public sourcecleaner_ExtensionPoint(
        String name,        String schema,        boolean diagraph,        String id    ) {
        this.name = name;
        this.schema = schema;
        this.diagraph = diagraph;
        this.id = id;
        this.sourcecleaner_extensions = new ArrayList<>();
    }

    public sourcecleaner_ExtensionPoint(
        String name,        String schema,        boolean diagraph,        String id        ArrayList<sourcecleaner_Extension> sourcecleaner_extensions    ) {
        this.name = name;
        this.schema = schema;
        this.diagraph = diagraph;
        this.id = id;
        this.sourcecleaner_extensions = sourcecleaner_extensions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSchema() {
        return schema;
    }

    public void setSchema(String schema) {
        this.schema = schema;
    }
    public boolean getDiagraph() {
        return diagraph;
    }

    public void setDiagraph(boolean diagraph) {
        this.diagraph = diagraph;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public sourcecleaner_Plugin getSourcecleaner_plugin() {
        return sourcecleaner_plugin;
    }

    public void setSourcecleaner_plugin(sourcecleaner_Plugin sourcecleaner_plugin) {
        this.sourcecleaner_plugin = sourcecleaner_plugin;
    }
    public sourcecleaner_Plugin getSourcecleaner_plugin() {
        return sourcecleaner_plugin;
    }

    public void setSourcecleaner_plugin(sourcecleaner_Plugin sourcecleaner_plugin) {
        this.sourcecleaner_plugin = sourcecleaner_plugin;
    }
    public sourcecleaner_Extension getSourcecleaner_extension() {
        return sourcecleaner_extension;
    }

    public void setSourcecleaner_extension(sourcecleaner_Extension sourcecleaner_extension) {
        this.sourcecleaner_extension = sourcecleaner_extension;
    }
    public List<sourcecleaner_Extension> getSourcecleaner_extensions() {
        return sourcecleaner_extensions;
    }

    public void addSourcecleaner_extension(Sourcecleaner_extension sourcecleaner_extension) {
        this.sourcecleaner_extensions.add(sourcecleaner_extension);
    }

}
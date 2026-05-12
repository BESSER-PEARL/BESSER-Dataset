





import java.util.List;
import java.util.ArrayList;

public class sourcecleaner_Project extends LocatedElement {

    private String workspace;
    private int id;





    private sourcecleaner_Manifest sourcecleaner_manifest;




    private sourcecleaner_Plugin sourcecleaner_plugin;




    private sourcecleaner_Configuration sourcecleaner_configuration;




    private sourcecleaner_Plugin sourcecleaner_plugin;




    private sourcecleaner_Build sourcecleaner_build;




    private sourcecleaner_Java sourcecleaner_java;




    private List<sourcecleaner_Java> sourcecleaner_javas;


    public sourcecleaner_Project(
        String workspace,        int id    ) {
        super(
        );
        this.workspace = workspace;
        this.id = id;
        this.sourcecleaner_javas = new ArrayList<>();
    }

    public sourcecleaner_Project(
        String workspace,        int id        ArrayList<sourcecleaner_Java> sourcecleaner_javas    ) {
        this.workspace = workspace;
        this.id = id;
        this.sourcecleaner_javas = sourcecleaner_javas;
    }

    public String getWorkspace() {
        return workspace;
    }

    public void setWorkspace(String workspace) {
        this.workspace = workspace;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public sourcecleaner_Manifest getSourcecleaner_manifest() {
        return sourcecleaner_manifest;
    }

    public void setSourcecleaner_manifest(sourcecleaner_Manifest sourcecleaner_manifest) {
        this.sourcecleaner_manifest = sourcecleaner_manifest;
    }
    public sourcecleaner_Plugin getSourcecleaner_plugin() {
        return sourcecleaner_plugin;
    }

    public void setSourcecleaner_plugin(sourcecleaner_Plugin sourcecleaner_plugin) {
        this.sourcecleaner_plugin = sourcecleaner_plugin;
    }
    public sourcecleaner_Configuration getSourcecleaner_configuration() {
        return sourcecleaner_configuration;
    }

    public void setSourcecleaner_configuration(sourcecleaner_Configuration sourcecleaner_configuration) {
        this.sourcecleaner_configuration = sourcecleaner_configuration;
    }
    public sourcecleaner_Plugin getSourcecleaner_plugin() {
        return sourcecleaner_plugin;
    }

    public void setSourcecleaner_plugin(sourcecleaner_Plugin sourcecleaner_plugin) {
        this.sourcecleaner_plugin = sourcecleaner_plugin;
    }
    public sourcecleaner_Build getSourcecleaner_build() {
        return sourcecleaner_build;
    }

    public void setSourcecleaner_build(sourcecleaner_Build sourcecleaner_build) {
        this.sourcecleaner_build = sourcecleaner_build;
    }
    public sourcecleaner_Java getSourcecleaner_java() {
        return sourcecleaner_java;
    }

    public void setSourcecleaner_java(sourcecleaner_Java sourcecleaner_java) {
        this.sourcecleaner_java = sourcecleaner_java;
    }
    public List<sourcecleaner_Java> getSourcecleaner_javas() {
        return sourcecleaner_javas;
    }

    public void addSourcecleaner_java(Sourcecleaner_java sourcecleaner_java) {
        this.sourcecleaner_javas.add(sourcecleaner_java);
    }

}
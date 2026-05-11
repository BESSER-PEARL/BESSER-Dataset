





import java.util.List;
import java.util.ArrayList;

public class editormodel_FlabotFileModel extends ExtensibleElement {

    private String provider;
    private String version;
    private String id;
    private String name;





    private editormodel_Folder editormodel_folder;




    private editormodel_Folder editormodel_folder;




    private editormodel_FlabotFileModel editormodel_flabotfilemodel;




    private List<editormodel_Diagram> editormodel_diagrams;




    private List<editormodel_Diagram> editormodel_diagrams;




    private editormodel_CoreModel editormodel_coremodel;


    public editormodel_FlabotFileModel(
        String provider,        String version,        String id,        String name    ) {
        super(
        );
        this.provider = provider;
        this.version = version;
        this.id = id;
        this.name = name;
        this.editormodel_diagrams = new ArrayList<>();
        this.editormodel_diagrams = new ArrayList<>();
    }

    public editormodel_FlabotFileModel(
        String provider,        String version,        String id,        String name        ArrayList<editormodel_Diagram> editormodel_diagrams,        ArrayList<editormodel_Diagram> editormodel_diagrams    ) {
        this.provider = provider;
        this.version = version;
        this.id = id;
        this.name = name;
        this.editormodel_diagrams = editormodel_diagrams;
        this.editormodel_diagrams = editormodel_diagrams;
    }

    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public editormodel_Folder getEditormodel_folder() {
        return editormodel_folder;
    }

    public void setEditormodel_folder(editormodel_Folder editormodel_folder) {
        this.editormodel_folder = editormodel_folder;
    }
    public editormodel_Folder getEditormodel_folder() {
        return editormodel_folder;
    }

    public void setEditormodel_folder(editormodel_Folder editormodel_folder) {
        this.editormodel_folder = editormodel_folder;
    }
    public editormodel_FlabotFileModel getEditormodel_flabotfilemodel() {
        return editormodel_flabotfilemodel;
    }

    public void setEditormodel_flabotfilemodel(editormodel_FlabotFileModel editormodel_flabotfilemodel) {
        this.editormodel_flabotfilemodel = editormodel_flabotfilemodel;
    }
    public List<editormodel_Diagram> getEditormodel_diagrams() {
        return editormodel_diagrams;
    }

    public void addEditormodel_diagram(Editormodel_diagram editormodel_diagram) {
        this.editormodel_diagrams.add(editormodel_diagram);
    }
    public List<editormodel_Diagram> getEditormodel_diagrams() {
        return editormodel_diagrams;
    }

    public void addEditormodel_diagram(Editormodel_diagram editormodel_diagram) {
        this.editormodel_diagrams.add(editormodel_diagram);
    }
    public editormodel_CoreModel getEditormodel_coremodel() {
        return editormodel_coremodel;
    }

    public void setEditormodel_coremodel(editormodel_CoreModel editormodel_coremodel) {
        this.editormodel_coremodel = editormodel_coremodel;
    }

}
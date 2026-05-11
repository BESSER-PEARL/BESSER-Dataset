





import java.util.List;
import java.util.ArrayList;

public class editormodel_Folder  {

    private String name;





    private List<editormodel_Folder> editormodel_folders;




    private editormodel_Folder editormodel_folder;




    private List<editormodel_Diagram> editormodel_diagrams;




    private editormodel_Diagram editormodel_diagram;


    public editormodel_Folder(
        String name    ) {
        this.name = name;
        this.editormodel_folders = new ArrayList<>();
        this.editormodel_diagrams = new ArrayList<>();
    }

    public editormodel_Folder(
        String name        ArrayList<editormodel_Folder> editormodel_folders,        ArrayList<editormodel_Diagram> editormodel_diagrams    ) {
        this.name = name;
        this.editormodel_folders = editormodel_folders;
        this.editormodel_diagrams = editormodel_diagrams;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<editormodel_Folder> getEditormodel_folders() {
        return editormodel_folders;
    }

    public void addEditormodel_folder(Editormodel_folder editormodel_folder) {
        this.editormodel_folders.add(editormodel_folder);
    }
    public editormodel_Folder getEditormodel_folder() {
        return editormodel_folder;
    }

    public void setEditormodel_folder(editormodel_Folder editormodel_folder) {
        this.editormodel_folder = editormodel_folder;
    }
    public List<editormodel_Diagram> getEditormodel_diagrams() {
        return editormodel_diagrams;
    }

    public void addEditormodel_diagram(Editormodel_diagram editormodel_diagram) {
        this.editormodel_diagrams.add(editormodel_diagram);
    }
    public editormodel_Diagram getEditormodel_diagram() {
        return editormodel_diagram;
    }

    public void setEditormodel_diagram(editormodel_Diagram editormodel_diagram) {
        this.editormodel_diagram = editormodel_diagram;
    }

}
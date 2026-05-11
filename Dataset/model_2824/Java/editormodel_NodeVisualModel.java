





import java.util.List;
import java.util.ArrayList;

public class editormodel_NodeVisualModel extends VisualModel {

    private String rotation;





    private editormodel_ConnectionVisualModel editormodel_connectionvisualmodel;




    private editormodel_VisualDiagramJump editormodel_visualdiagramjump;




    private editormodel_ConnectionVisualModel editormodel_connectionvisualmodel;




    private List<editormodel_ConnectionVisualModel> editormodel_connectionvisualmodels;




    private List<editormodel_ConnectionVisualModel> editormodel_connectionvisualmodels;


    public editormodel_NodeVisualModel(
        String rotation    ) {
        super(
        );
        this.rotation = rotation;
        this.editormodel_connectionvisualmodels = new ArrayList<>();
        this.editormodel_connectionvisualmodels = new ArrayList<>();
    }

    public editormodel_NodeVisualModel(
        String rotation        ArrayList<editormodel_ConnectionVisualModel> editormodel_connectionvisualmodels,        ArrayList<editormodel_ConnectionVisualModel> editormodel_connectionvisualmodels    ) {
        this.rotation = rotation;
        this.editormodel_connectionvisualmodels = editormodel_connectionvisualmodels;
        this.editormodel_connectionvisualmodels = editormodel_connectionvisualmodels;
    }

    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }

    public editormodel_ConnectionVisualModel getEditormodel_connectionvisualmodel() {
        return editormodel_connectionvisualmodel;
    }

    public void setEditormodel_connectionvisualmodel(editormodel_ConnectionVisualModel editormodel_connectionvisualmodel) {
        this.editormodel_connectionvisualmodel = editormodel_connectionvisualmodel;
    }
    public editormodel_VisualDiagramJump getEditormodel_visualdiagramjump() {
        return editormodel_visualdiagramjump;
    }

    public void setEditormodel_visualdiagramjump(editormodel_VisualDiagramJump editormodel_visualdiagramjump) {
        this.editormodel_visualdiagramjump = editormodel_visualdiagramjump;
    }
    public editormodel_ConnectionVisualModel getEditormodel_connectionvisualmodel() {
        return editormodel_connectionvisualmodel;
    }

    public void setEditormodel_connectionvisualmodel(editormodel_ConnectionVisualModel editormodel_connectionvisualmodel) {
        this.editormodel_connectionvisualmodel = editormodel_connectionvisualmodel;
    }
    public List<editormodel_ConnectionVisualModel> getEditormodel_connectionvisualmodels() {
        return editormodel_connectionvisualmodels;
    }

    public void addEditormodel_connectionvisualmodel(Editormodel_connectionvisualmodel editormodel_connectionvisualmodel) {
        this.editormodel_connectionvisualmodels.add(editormodel_connectionvisualmodel);
    }
    public List<editormodel_ConnectionVisualModel> getEditormodel_connectionvisualmodels() {
        return editormodel_connectionvisualmodels;
    }

    public void addEditormodel_connectionvisualmodel(Editormodel_connectionvisualmodel editormodel_connectionvisualmodel) {
        this.editormodel_connectionvisualmodels.add(editormodel_connectionvisualmodel);
    }

}
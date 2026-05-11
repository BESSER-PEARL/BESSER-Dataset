





import java.util.List;
import java.util.ArrayList;

public class editormodel_ConnectionVisualModel extends NodeVisualModel {

    private String sourceTerminal;
    private String targetTerminal;





    private List<editormodel_ConnectionBendpoint> editormodel_connectionbendpoints;




    private editormodel_NodeVisualModel editormodel_nodevisualmodel;




    private editormodel_NodeVisualModel editormodel_nodevisualmodel;




    private editormodel_NodeVisualModel editormodel_nodevisualmodel;




    private editormodel_NodeVisualModel editormodel_nodevisualmodel;


    public editormodel_ConnectionVisualModel(
        String sourceTerminal,        String targetTerminal    ) {
        super(
        );
        this.sourceTerminal = sourceTerminal;
        this.targetTerminal = targetTerminal;
        this.editormodel_connectionbendpoints = new ArrayList<>();
    }

    public editormodel_ConnectionVisualModel(
        String sourceTerminal,        String targetTerminal        ArrayList<editormodel_ConnectionBendpoint> editormodel_connectionbendpoints    ) {
        this.sourceTerminal = sourceTerminal;
        this.targetTerminal = targetTerminal;
        this.editormodel_connectionbendpoints = editormodel_connectionbendpoints;
    }

    public String getSourceterminal() {
        return sourceTerminal;
    }

    public void setSourceterminal(String sourceTerminal) {
        this.sourceTerminal = sourceTerminal;
    }
    public String getTargetterminal() {
        return targetTerminal;
    }

    public void setTargetterminal(String targetTerminal) {
        this.targetTerminal = targetTerminal;
    }

    public List<editormodel_ConnectionBendpoint> getEditormodel_connectionbendpoints() {
        return editormodel_connectionbendpoints;
    }

    public void addEditormodel_connectionbendpoint(Editormodel_connectionbendpoint editormodel_connectionbendpoint) {
        this.editormodel_connectionbendpoints.add(editormodel_connectionbendpoint);
    }
    public editormodel_NodeVisualModel getEditormodel_nodevisualmodel() {
        return editormodel_nodevisualmodel;
    }

    public void setEditormodel_nodevisualmodel(editormodel_NodeVisualModel editormodel_nodevisualmodel) {
        this.editormodel_nodevisualmodel = editormodel_nodevisualmodel;
    }
    public editormodel_NodeVisualModel getEditormodel_nodevisualmodel() {
        return editormodel_nodevisualmodel;
    }

    public void setEditormodel_nodevisualmodel(editormodel_NodeVisualModel editormodel_nodevisualmodel) {
        this.editormodel_nodevisualmodel = editormodel_nodevisualmodel;
    }
    public editormodel_NodeVisualModel getEditormodel_nodevisualmodel() {
        return editormodel_nodevisualmodel;
    }

    public void setEditormodel_nodevisualmodel(editormodel_NodeVisualModel editormodel_nodevisualmodel) {
        this.editormodel_nodevisualmodel = editormodel_nodevisualmodel;
    }
    public editormodel_NodeVisualModel getEditormodel_nodevisualmodel() {
        return editormodel_nodevisualmodel;
    }

    public void setEditormodel_nodevisualmodel(editormodel_NodeVisualModel editormodel_nodevisualmodel) {
        this.editormodel_nodevisualmodel = editormodel_nodevisualmodel;
    }

}
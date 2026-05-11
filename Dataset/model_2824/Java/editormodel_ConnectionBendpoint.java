





import java.util.List;
import java.util.ArrayList;

public class editormodel_ConnectionBendpoint  {

    private float weight;





    private editormodel_Dimension editormodel_dimension;




    private editormodel_ConnectionVisualModel editormodel_connectionvisualmodel;




    private editormodel_Dimension editormodel_dimension;


    public editormodel_ConnectionBendpoint(
        float weight    ) {
        this.weight = weight;
    }


    public float getWeight() {
        return weight;
    }

    public void setWeight(float weight) {
        this.weight = weight;
    }

    public editormodel_Dimension getEditormodel_dimension() {
        return editormodel_dimension;
    }

    public void setEditormodel_dimension(editormodel_Dimension editormodel_dimension) {
        this.editormodel_dimension = editormodel_dimension;
    }
    public editormodel_ConnectionVisualModel getEditormodel_connectionvisualmodel() {
        return editormodel_connectionvisualmodel;
    }

    public void setEditormodel_connectionvisualmodel(editormodel_ConnectionVisualModel editormodel_connectionvisualmodel) {
        this.editormodel_connectionvisualmodel = editormodel_connectionvisualmodel;
    }
    public editormodel_Dimension getEditormodel_dimension() {
        return editormodel_dimension;
    }

    public void setEditormodel_dimension(editormodel_Dimension editormodel_dimension) {
        this.editormodel_dimension = editormodel_dimension;
    }

}
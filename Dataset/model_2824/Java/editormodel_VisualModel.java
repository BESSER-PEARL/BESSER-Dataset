





import java.util.List;
import java.util.ArrayList;

public class editormodel_VisualModel extends Adapter {

    private int lineWidth;
    private int detailLevel;
    private int lineStyle;





    private editormodel_VisualModel editormodel_visualmodel;




    private editormodel_Diagram editormodel_diagram;




    private editormodel_Diagram editormodel_diagram;




    private List<editormodel_VisualModel> editormodel_visualmodels;


    public editormodel_VisualModel(
        int lineWidth,        int detailLevel,        int lineStyle    ) {
        super(
        );
        this.lineWidth = lineWidth;
        this.detailLevel = detailLevel;
        this.lineStyle = lineStyle;
        this.editormodel_visualmodels = new ArrayList<>();
    }

    public editormodel_VisualModel(
        int lineWidth,        int detailLevel,        int lineStyle        ArrayList<editormodel_VisualModel> editormodel_visualmodels    ) {
        this.lineWidth = lineWidth;
        this.detailLevel = detailLevel;
        this.lineStyle = lineStyle;
        this.editormodel_visualmodels = editormodel_visualmodels;
    }

    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }
    public int getDetaillevel() {
        return detailLevel;
    }

    public void setDetaillevel(int detailLevel) {
        this.detailLevel = detailLevel;
    }
    public int getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(int lineStyle) {
        this.lineStyle = lineStyle;
    }

    public editormodel_VisualModel getEditormodel_visualmodel() {
        return editormodel_visualmodel;
    }

    public void setEditormodel_visualmodel(editormodel_VisualModel editormodel_visualmodel) {
        this.editormodel_visualmodel = editormodel_visualmodel;
    }
    public editormodel_Diagram getEditormodel_diagram() {
        return editormodel_diagram;
    }

    public void setEditormodel_diagram(editormodel_Diagram editormodel_diagram) {
        this.editormodel_diagram = editormodel_diagram;
    }
    public editormodel_Diagram getEditormodel_diagram() {
        return editormodel_diagram;
    }

    public void setEditormodel_diagram(editormodel_Diagram editormodel_diagram) {
        this.editormodel_diagram = editormodel_diagram;
    }
    public List<editormodel_VisualModel> getEditormodel_visualmodels() {
        return editormodel_visualmodels;
    }

    public void addEditormodel_visualmodel(Editormodel_visualmodel editormodel_visualmodel) {
        this.editormodel_visualmodels.add(editormodel_visualmodel);
    }

}
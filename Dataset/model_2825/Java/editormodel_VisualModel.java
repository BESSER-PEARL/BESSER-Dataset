





import java.util.List;
import java.util.ArrayList;

public class editormodel_VisualModel extends Adapter {

    private int lineStyle;
    private int detailLevel;
    private int lineWidth;





    private editormodel_VisualModel editormodel_visualmodel;




    private List<editormodel_VisualModel> editormodel_visualmodels;


    public editormodel_VisualModel(
        int lineStyle,        int detailLevel,        int lineWidth    ) {
        super(
        );
        this.lineStyle = lineStyle;
        this.detailLevel = detailLevel;
        this.lineWidth = lineWidth;
        this.editormodel_visualmodels = new ArrayList<>();
    }

    public editormodel_VisualModel(
        int lineStyle,        int detailLevel,        int lineWidth        ArrayList<editormodel_VisualModel> editormodel_visualmodels    ) {
        this.lineStyle = lineStyle;
        this.detailLevel = detailLevel;
        this.lineWidth = lineWidth;
        this.editormodel_visualmodels = editormodel_visualmodels;
    }

    public int getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(int lineStyle) {
        this.lineStyle = lineStyle;
    }
    public int getDetaillevel() {
        return detailLevel;
    }

    public void setDetaillevel(int detailLevel) {
        this.detailLevel = detailLevel;
    }
    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }

    public editormodel_VisualModel getEditormodel_visualmodel() {
        return editormodel_visualmodel;
    }

    public void setEditormodel_visualmodel(editormodel_VisualModel editormodel_visualmodel) {
        this.editormodel_visualmodel = editormodel_visualmodel;
    }
    public List<editormodel_VisualModel> getEditormodel_visualmodels() {
        return editormodel_visualmodels;
    }

    public void addEditormodel_visualmodel(Editormodel_visualmodel editormodel_visualmodel) {
        this.editormodel_visualmodels.add(editormodel_visualmodel);
    }

}
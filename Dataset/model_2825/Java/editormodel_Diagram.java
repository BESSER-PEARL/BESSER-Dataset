





import java.util.List;
import java.util.ArrayList;

public class editormodel_Diagram extends NamedElementModel {

    private String gridEnabled;
    private String snapToGeometryEnabled;





    private editormodel_VisualModel editormodel_visualmodel;




    private List<editormodel_VisualModel> editormodel_visualmodels;


    public editormodel_Diagram(
        String gridEnabled,        String snapToGeometryEnabled    ) {
        super(
        );
        this.gridEnabled = gridEnabled;
        this.snapToGeometryEnabled = snapToGeometryEnabled;
        this.editormodel_visualmodels = new ArrayList<>();
    }

    public editormodel_Diagram(
        String gridEnabled,        String snapToGeometryEnabled        ArrayList<editormodel_VisualModel> editormodel_visualmodels    ) {
        this.gridEnabled = gridEnabled;
        this.snapToGeometryEnabled = snapToGeometryEnabled;
        this.editormodel_visualmodels = editormodel_visualmodels;
    }

    public String getGridenabled() {
        return gridEnabled;
    }

    public void setGridenabled(String gridEnabled) {
        this.gridEnabled = gridEnabled;
    }
    public String getSnaptogeometryenabled() {
        return snapToGeometryEnabled;
    }

    public void setSnaptogeometryenabled(String snapToGeometryEnabled) {
        this.snapToGeometryEnabled = snapToGeometryEnabled;
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
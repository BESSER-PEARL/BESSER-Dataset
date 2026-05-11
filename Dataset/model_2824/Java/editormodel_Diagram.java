





import java.util.List;
import java.util.ArrayList;

public class editormodel_Diagram extends NamedElementModel {

    private String gridEnabled;
    private String snapToGeometryEnabled;



    public editormodel_Diagram(
        String gridEnabled,        String snapToGeometryEnabled    ) {
        super(
        );
        this.gridEnabled = gridEnabled;
        this.snapToGeometryEnabled = snapToGeometryEnabled;
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


}
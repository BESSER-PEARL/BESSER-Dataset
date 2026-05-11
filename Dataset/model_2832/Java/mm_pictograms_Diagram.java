





import java.util.List;
import java.util.ArrayList;

public class mm_pictograms_Diagram extends pictograms_ContainerShape, StyleContainer {

    private boolean snapToGrid;
    private int verticalGridUnit;
    private String diagramTypeId;
    private int gridUnit;
    private String version;
    private String name;
    private boolean showGuides;



    public mm_pictograms_Diagram(
        boolean snapToGrid,        int verticalGridUnit,        String diagramTypeId,        int gridUnit,        String version,        String name,        boolean showGuides    ) {
        super(
        );
        this.snapToGrid = snapToGrid;
        this.verticalGridUnit = verticalGridUnit;
        this.diagramTypeId = diagramTypeId;
        this.gridUnit = gridUnit;
        this.version = version;
        this.name = name;
        this.showGuides = showGuides;
    }


    public boolean getSnaptogrid() {
        return snapToGrid;
    }

    public void setSnaptogrid(boolean snapToGrid) {
        this.snapToGrid = snapToGrid;
    }
    public int getVerticalgridunit() {
        return verticalGridUnit;
    }

    public void setVerticalgridunit(int verticalGridUnit) {
        this.verticalGridUnit = verticalGridUnit;
    }
    public String getDiagramtypeid() {
        return diagramTypeId;
    }

    public void setDiagramtypeid(String diagramTypeId) {
        this.diagramTypeId = diagramTypeId;
    }
    public int getGridunit() {
        return gridUnit;
    }

    public void setGridunit(int gridUnit) {
        this.gridUnit = gridUnit;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getShowguides() {
        return showGuides;
    }

    public void setShowguides(boolean showGuides) {
        this.showGuides = showGuides;
    }


}
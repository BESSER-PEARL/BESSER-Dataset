





import java.util.List;
import java.util.ArrayList;

public class mm_pictograms_Diagram extends pictograms_ContainerShape, StyleContainer {

    private boolean snapToGrid;
    private String version;
    private String diagramTypeId;
    private boolean showGuides;
    private String name;
    private int gridUnit;
    private int verticalGridUnit;



    public mm_pictograms_Diagram(
        boolean snapToGrid,        String version,        String diagramTypeId,        boolean showGuides,        String name,        int gridUnit,        int verticalGridUnit    ) {
        super(
        );
        this.snapToGrid = snapToGrid;
        this.version = version;
        this.diagramTypeId = diagramTypeId;
        this.showGuides = showGuides;
        this.name = name;
        this.gridUnit = gridUnit;
        this.verticalGridUnit = verticalGridUnit;
    }


    public boolean getSnaptogrid() {
        return snapToGrid;
    }

    public void setSnaptogrid(boolean snapToGrid) {
        this.snapToGrid = snapToGrid;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getDiagramtypeid() {
        return diagramTypeId;
    }

    public void setDiagramtypeid(String diagramTypeId) {
        this.diagramTypeId = diagramTypeId;
    }
    public boolean getShowguides() {
        return showGuides;
    }

    public void setShowguides(boolean showGuides) {
        this.showGuides = showGuides;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getGridunit() {
        return gridUnit;
    }

    public void setGridunit(int gridUnit) {
        this.gridUnit = gridUnit;
    }
    public int getVerticalgridunit() {
        return verticalGridUnit;
    }

    public void setVerticalgridunit(int verticalGridUnit) {
        this.verticalGridUnit = verticalGridUnit;
    }


}
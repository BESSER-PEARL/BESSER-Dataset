





import java.util.List;
import java.util.ArrayList;

public class mm_pictograms_Diagram extends pictograms_ContainerShape, StyleContainer {

    private String diagramTypeId;
    private boolean snapToGrid;
    private int verticalGridUnit;
    private String name;
    private boolean showGuides;
    private String version;
    private int gridUnit;



    public mm_pictograms_Diagram(
        String diagramTypeId,        boolean snapToGrid,        int verticalGridUnit,        String name,        boolean showGuides,        String version,        int gridUnit    ) {
        super(
        );
        this.diagramTypeId = diagramTypeId;
        this.snapToGrid = snapToGrid;
        this.verticalGridUnit = verticalGridUnit;
        this.name = name;
        this.showGuides = showGuides;
        this.version = version;
        this.gridUnit = gridUnit;
    }


    public String getDiagramtypeid() {
        return diagramTypeId;
    }

    public void setDiagramtypeid(String diagramTypeId) {
        this.diagramTypeId = diagramTypeId;
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
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public int getGridunit() {
        return gridUnit;
    }

    public void setGridunit(int gridUnit) {
        this.gridUnit = gridUnit;
    }


}
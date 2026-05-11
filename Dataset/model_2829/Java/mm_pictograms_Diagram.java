





import java.util.List;
import java.util.ArrayList;

public class mm_pictograms_Diagram extends StyleContainer, pictograms_ContainerShape {

    private boolean snapToGrid;
    private String diagramTypeId;
    private String name;
    private int gridUnit;
    private String version;
    private boolean showGuides;
    private int verticalGridUnit;



    public mm_pictograms_Diagram(
        boolean snapToGrid,        String diagramTypeId,        String name,        int gridUnit,        String version,        boolean showGuides,        int verticalGridUnit    ) {
        super(
        );
        this.snapToGrid = snapToGrid;
        this.diagramTypeId = diagramTypeId;
        this.name = name;
        this.gridUnit = gridUnit;
        this.version = version;
        this.showGuides = showGuides;
        this.verticalGridUnit = verticalGridUnit;
    }


    public boolean getSnaptogrid() {
        return snapToGrid;
    }

    public void setSnaptogrid(boolean snapToGrid) {
        this.snapToGrid = snapToGrid;
    }
    public String getDiagramtypeid() {
        return diagramTypeId;
    }

    public void setDiagramtypeid(String diagramTypeId) {
        this.diagramTypeId = diagramTypeId;
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
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public boolean getShowguides() {
        return showGuides;
    }

    public void setShowguides(boolean showGuides) {
        this.showGuides = showGuides;
    }
    public int getVerticalgridunit() {
        return verticalGridUnit;
    }

    public void setVerticalgridunit(int verticalGridUnit) {
        this.verticalGridUnit = verticalGridUnit;
    }


}
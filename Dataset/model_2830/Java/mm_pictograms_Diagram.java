





import java.util.List;
import java.util.ArrayList;

public class mm_pictograms_Diagram extends StyleContainer, pictograms_ContainerShape {

    private String version;
    private int verticalGridUnit;
    private boolean showGuides;
    private String diagramTypeId;
    private boolean snapToGrid;
    private int gridUnit;
    private String name;





    private List<PictogramLink> pictogramlinks;


    public mm_pictograms_Diagram(
        String version,        int verticalGridUnit,        boolean showGuides,        String diagramTypeId,        boolean snapToGrid,        int gridUnit,        String name    ) {
        super(
        );
        this.version = version;
        this.verticalGridUnit = verticalGridUnit;
        this.showGuides = showGuides;
        this.diagramTypeId = diagramTypeId;
        this.snapToGrid = snapToGrid;
        this.gridUnit = gridUnit;
        this.name = name;
        this.pictogramlinks = new ArrayList<>();
    }

    public mm_pictograms_Diagram(
        String version,        int verticalGridUnit,        boolean showGuides,        String diagramTypeId,        boolean snapToGrid,        int gridUnit,        String name        ArrayList<PictogramLink> pictogramlinks    ) {
        this.version = version;
        this.verticalGridUnit = verticalGridUnit;
        this.showGuides = showGuides;
        this.diagramTypeId = diagramTypeId;
        this.snapToGrid = snapToGrid;
        this.gridUnit = gridUnit;
        this.name = name;
        this.pictogramlinks = pictogramlinks;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public int getVerticalgridunit() {
        return verticalGridUnit;
    }

    public void setVerticalgridunit(int verticalGridUnit) {
        this.verticalGridUnit = verticalGridUnit;
    }
    public boolean getShowguides() {
        return showGuides;
    }

    public void setShowguides(boolean showGuides) {
        this.showGuides = showGuides;
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
    public int getGridunit() {
        return gridUnit;
    }

    public void setGridunit(int gridUnit) {
        this.gridUnit = gridUnit;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<PictogramLink> getPictogramlinks() {
        return pictogramlinks;
    }

    public void addPictogramlink(Pictogramlink pictogramlink) {
        this.pictogramlinks.add(pictogramlink);
    }

}
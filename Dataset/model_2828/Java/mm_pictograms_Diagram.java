





import java.util.List;
import java.util.ArrayList;

public class mm_pictograms_Diagram extends StyleContainer, pictograms_ContainerShape {

    private String version;
    private int gridUnit;
    private String name;
    private String diagramTypeId;
    private boolean snapToGrid;
    private boolean showGuides;
    private int verticalGridUnit;





    private List<styles_Font> styles_fonts;




    private List<PictogramLink> pictogramlinks;




    private List<styles_Color> styles_colors;


    public mm_pictograms_Diagram(
        String version,        int gridUnit,        String name,        String diagramTypeId,        boolean snapToGrid,        boolean showGuides,        int verticalGridUnit    ) {
        super(
        );
        this.version = version;
        this.gridUnit = gridUnit;
        this.name = name;
        this.diagramTypeId = diagramTypeId;
        this.snapToGrid = snapToGrid;
        this.showGuides = showGuides;
        this.verticalGridUnit = verticalGridUnit;
        this.styles_fonts = new ArrayList<>();
        this.pictogramlinks = new ArrayList<>();
        this.styles_colors = new ArrayList<>();
    }

    public mm_pictograms_Diagram(
        String version,        int gridUnit,        String name,        String diagramTypeId,        boolean snapToGrid,        boolean showGuides,        int verticalGridUnit        ArrayList<styles_Font> styles_fonts,        ArrayList<PictogramLink> pictogramlinks,        ArrayList<styles_Color> styles_colors    ) {
        this.version = version;
        this.gridUnit = gridUnit;
        this.name = name;
        this.diagramTypeId = diagramTypeId;
        this.snapToGrid = snapToGrid;
        this.showGuides = showGuides;
        this.verticalGridUnit = verticalGridUnit;
        this.styles_fonts = styles_fonts;
        this.pictogramlinks = pictogramlinks;
        this.styles_colors = styles_colors;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public List<styles_Font> getStyles_fonts() {
        return styles_fonts;
    }

    public void addStyles_font(Styles_font styles_font) {
        this.styles_fonts.add(styles_font);
    }
    public List<PictogramLink> getPictogramlinks() {
        return pictogramlinks;
    }

    public void addPictogramlink(Pictogramlink pictogramlink) {
        this.pictogramlinks.add(pictogramlink);
    }
    public List<styles_Color> getStyles_colors() {
        return styles_colors;
    }

    public void addStyles_color(Styles_color styles_color) {
        this.styles_colors.add(styles_color);
    }

}






import java.util.List;
import java.util.ArrayList;

public class di_Diagram extends Container {

    private boolean snapToGrid;
    private boolean snapToGeometry;
    private String rulers;





    private List<di_CommentLink> di_commentlinks;


    public di_Diagram(
        boolean snapToGrid,        boolean snapToGeometry,        String rulers    ) {
        super(
        );
        this.snapToGrid = snapToGrid;
        this.snapToGeometry = snapToGeometry;
        this.rulers = rulers;
        this.di_commentlinks = new ArrayList<>();
    }

    public di_Diagram(
        boolean snapToGrid,        boolean snapToGeometry,        String rulers        ArrayList<di_CommentLink> di_commentlinks    ) {
        this.snapToGrid = snapToGrid;
        this.snapToGeometry = snapToGeometry;
        this.rulers = rulers;
        this.di_commentlinks = di_commentlinks;
    }

    public boolean getSnaptogrid() {
        return snapToGrid;
    }

    public void setSnaptogrid(boolean snapToGrid) {
        this.snapToGrid = snapToGrid;
    }
    public boolean getSnaptogeometry() {
        return snapToGeometry;
    }

    public void setSnaptogeometry(boolean snapToGeometry) {
        this.snapToGeometry = snapToGeometry;
    }
    public String getRulers() {
        return rulers;
    }

    public void setRulers(String rulers) {
        this.rulers = rulers;
    }

    public List<di_CommentLink> getDi_commentlinks() {
        return di_commentlinks;
    }

    public void addDi_commentlink(Di_commentlink di_commentlink) {
        this.di_commentlinks.add(di_commentlink);
    }

}
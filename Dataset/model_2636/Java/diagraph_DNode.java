





import java.util.List;
import java.util.ArrayList;

public class diagraph_DNode extends DLabeledElement, DOwnedElement {

    private String shape;
    private boolean layout;
    private String navigationLink;





    private diagraph_DEdge diagraph_dedge;


    public diagraph_DNode(
        String shape,        boolean layout,        String navigationLink    ) {
        super(
        );
        this.shape = shape;
        this.layout = layout;
        this.navigationLink = navigationLink;
    }


    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public boolean getLayout() {
        return layout;
    }

    public void setLayout(boolean layout) {
        this.layout = layout;
    }
    public String getNavigationlink() {
        return navigationLink;
    }

    public void setNavigationlink(String navigationLink) {
        this.navigationLink = navigationLink;
    }

    public diagraph_DEdge getDiagraph_dedge() {
        return diagraph_dedge;
    }

    public void setDiagraph_dedge(diagraph_DEdge diagraph_dedge) {
        this.diagraph_dedge = diagraph_dedge;
    }

}
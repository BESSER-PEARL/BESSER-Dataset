





import java.util.List;
import java.util.ArrayList;

public class diagraph_DNode extends DLabeledElement, DOwnedElement {

    private String shape;
    private String navigationLink;
    private boolean layout;





    private diagraph_DEdge diagraph_dedge;




    private diagraph_DOwnedElement diagraph_downedelement;


    public diagraph_DNode(
        String shape,        String navigationLink,        boolean layout    ) {
        super(
        );
        this.shape = shape;
        this.navigationLink = navigationLink;
        this.layout = layout;
    }


    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public String getNavigationlink() {
        return navigationLink;
    }

    public void setNavigationlink(String navigationLink) {
        this.navigationLink = navigationLink;
    }
    public boolean getLayout() {
        return layout;
    }

    public void setLayout(boolean layout) {
        this.layout = layout;
    }

    public diagraph_DEdge getDiagraph_dedge() {
        return diagraph_dedge;
    }

    public void setDiagraph_dedge(diagraph_DEdge diagraph_dedge) {
        this.diagraph_dedge = diagraph_dedge;
    }
    public diagraph_DOwnedElement getDiagraph_downedelement() {
        return diagraph_downedelement;
    }

    public void setDiagraph_downedelement(diagraph_DOwnedElement diagraph_downedelement) {
        this.diagraph_downedelement = diagraph_downedelement;
    }

}
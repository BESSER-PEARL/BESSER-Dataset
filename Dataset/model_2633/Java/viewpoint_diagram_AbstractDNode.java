





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_AbstractDNode extends DDiagramElement {

    private String arrangeConstraints;



    public viewpoint_diagram_AbstractDNode(
        String arrangeConstraints    ) {
        super(
        );
        this.arrangeConstraints = arrangeConstraints;
    }


    public String getArrangeconstraints() {
        return arrangeConstraints;
    }

    public void setArrangeconstraints(String arrangeConstraints) {
        this.arrangeConstraints = arrangeConstraints;
    }


}
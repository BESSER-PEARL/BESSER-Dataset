





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_OrderedTreeLayout extends Layout {

    private String childrenExpression;





    private List<description_AbstractNodeMapping> description_abstractnodemappings;


    public viewpoint_description_OrderedTreeLayout(
        String childrenExpression    ) {
        super(
        );
        this.childrenExpression = childrenExpression;
        this.description_abstractnodemappings = new ArrayList<>();
    }

    public viewpoint_description_OrderedTreeLayout(
        String childrenExpression        ArrayList<description_AbstractNodeMapping> description_abstractnodemappings    ) {
        this.childrenExpression = childrenExpression;
        this.description_abstractnodemappings = description_abstractnodemappings;
    }

    public String getChildrenexpression() {
        return childrenExpression;
    }

    public void setChildrenexpression(String childrenExpression) {
        this.childrenExpression = childrenExpression;
    }

    public List<description_AbstractNodeMapping> getDescription_abstractnodemappings() {
        return description_abstractnodemappings;
    }

    public void addDescription_abstractnodemapping(Description_abstractnodemapping description_abstractnodemapping) {
        this.description_abstractnodemappings.add(description_abstractnodemapping);
    }

}
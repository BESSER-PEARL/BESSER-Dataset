





import java.util.List;
import java.util.ArrayList;

public class diagram_description_OrderedTreeLayout extends Layout {

    private String childrenExpression;





    private List<AbstractNodeMapping> abstractnodemappings;


    public diagram_description_OrderedTreeLayout(
        String childrenExpression    ) {
        super(
        );
        this.childrenExpression = childrenExpression;
        this.abstractnodemappings = new ArrayList<>();
    }

    public diagram_description_OrderedTreeLayout(
        String childrenExpression        ArrayList<AbstractNodeMapping> abstractnodemappings    ) {
        this.childrenExpression = childrenExpression;
        this.abstractnodemappings = abstractnodemappings;
    }

    public String getChildrenexpression() {
        return childrenExpression;
    }

    public void setChildrenexpression(String childrenExpression) {
        this.childrenExpression = childrenExpression;
    }

    public List<AbstractNodeMapping> getAbstractnodemappings() {
        return abstractnodemappings;
    }

    public void addAbstractnodemapping(Abstractnodemapping abstractnodemapping) {
        this.abstractnodemappings.add(abstractnodemapping);
    }

}
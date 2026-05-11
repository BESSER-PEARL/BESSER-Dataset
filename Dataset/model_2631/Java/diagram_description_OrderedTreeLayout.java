





import java.util.List;
import java.util.ArrayList;

public class diagram_description_OrderedTreeLayout extends Layout {

    private String childrenExpression;



    public diagram_description_OrderedTreeLayout(
        String childrenExpression    ) {
        super(
        );
        this.childrenExpression = childrenExpression;
    }


    public String getChildrenexpression() {
        return childrenExpression;
    }

    public void setChildrenexpression(String childrenExpression) {
        this.childrenExpression = childrenExpression;
    }


}
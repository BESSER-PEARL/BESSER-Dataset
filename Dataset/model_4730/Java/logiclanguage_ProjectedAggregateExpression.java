





import java.util.List;
import java.util.ArrayList;

public class logiclanguage_ProjectedAggregateExpression extends AggregateExpression {

    private int projectionIndex;



    public logiclanguage_ProjectedAggregateExpression(
        int projectionIndex    ) {
        super(
        );
        this.projectionIndex = projectionIndex;
    }


    public int getProjectionindex() {
        return projectionIndex;
    }

    public void setProjectionindex(int projectionIndex) {
        this.projectionIndex = projectionIndex;
    }


}
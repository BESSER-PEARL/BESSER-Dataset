





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_FormalParameter  {

    private boolean isOrdered;





    private OPLmetamodel_AggregateExp oplmetamodel_aggregateexp;


    public OPLmetamodel_FormalParameter(
        boolean isOrdered    ) {
        this.isOrdered = isOrdered;
    }


    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }

    public OPLmetamodel_AggregateExp getOplmetamodel_aggregateexp() {
        return oplmetamodel_aggregateexp;
    }

    public void setOplmetamodel_aggregateexp(OPLmetamodel_AggregateExp oplmetamodel_aggregateexp) {
        this.oplmetamodel_aggregateexp = oplmetamodel_aggregateexp;
    }

}
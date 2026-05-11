





import java.util.List;
import java.util.ArrayList;

public class frontend_core_TraceCompareExpression  {

    private boolean multivaluedTag;





    private Expression expression;




    private TraceElement traceelement;


    public frontend_core_TraceCompareExpression(
        boolean multivaluedTag    ) {
        this.multivaluedTag = multivaluedTag;
    }


    public boolean getMultivaluedtag() {
        return multivaluedTag;
    }

    public void setMultivaluedtag(boolean multivaluedTag) {
        this.multivaluedTag = multivaluedTag;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }
    public TraceElement getTraceelement() {
        return traceelement;
    }

    public void setTraceelement(TraceElement traceelement) {
        this.traceelement = traceelement;
    }

}
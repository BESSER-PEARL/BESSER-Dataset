





import java.util.List;
import java.util.ArrayList;

public class core_TraceCompareExpression  {

    private boolean multivaluedTag;





    private core_Expression core_expression;




    private core_TraceElement core_traceelement;




    private core_MatchTrace core_matchtrace;


    public core_TraceCompareExpression(
        boolean multivaluedTag    ) {
        this.multivaluedTag = multivaluedTag;
    }


    public boolean getMultivaluedtag() {
        return multivaluedTag;
    }

    public void setMultivaluedtag(boolean multivaluedTag) {
        this.multivaluedTag = multivaluedTag;
    }

    public core_Expression getCore_expression() {
        return core_expression;
    }

    public void setCore_expression(core_Expression core_expression) {
        this.core_expression = core_expression;
    }
    public core_TraceElement getCore_traceelement() {
        return core_traceelement;
    }

    public void setCore_traceelement(core_TraceElement core_traceelement) {
        this.core_traceelement = core_traceelement;
    }
    public core_MatchTrace getCore_matchtrace() {
        return core_matchtrace;
    }

    public void setCore_matchtrace(core_MatchTrace core_matchtrace) {
        this.core_matchtrace = core_matchtrace;
    }

}
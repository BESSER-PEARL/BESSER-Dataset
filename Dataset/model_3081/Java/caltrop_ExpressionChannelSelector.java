





import java.util.List;
import java.util.ArrayList;

public class caltrop_ExpressionChannelSelector extends ChannelSelector {

    private boolean many;





    private List<caltrop_XExpression> caltrop_xexpressions;


    public caltrop_ExpressionChannelSelector(
        boolean many    ) {
        super(
        );
        this.many = many;
        this.caltrop_xexpressions = new ArrayList<>();
    }

    public caltrop_ExpressionChannelSelector(
        boolean many        ArrayList<caltrop_XExpression> caltrop_xexpressions    ) {
        this.many = many;
        this.caltrop_xexpressions = caltrop_xexpressions;
    }

    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }

    public List<caltrop_XExpression> getCaltrop_xexpressions() {
        return caltrop_xexpressions;
    }

    public void addCaltrop_xexpression(Caltrop_xexpression caltrop_xexpression) {
        this.caltrop_xexpressions.add(caltrop_xexpression);
    }

}
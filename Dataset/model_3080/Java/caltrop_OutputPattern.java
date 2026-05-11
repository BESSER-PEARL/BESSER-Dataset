





import java.util.List;
import java.util.ArrayList;

public class caltrop_OutputPattern extends PortPattern {






    private List<caltrop_XExpression> caltrop_xexpressions;




    private caltrop_OutputAction caltrop_outputaction;


    public caltrop_OutputPattern(
    ) {
        super(
        );
        this.caltrop_xexpressions = new ArrayList<>();
    }

    public caltrop_OutputPattern(
        ArrayList<caltrop_XExpression> caltrop_xexpressions    ) {
        this.caltrop_xexpressions = caltrop_xexpressions;
    }


    public List<caltrop_XExpression> getCaltrop_xexpressions() {
        return caltrop_xexpressions;
    }

    public void addCaltrop_xexpression(Caltrop_xexpression caltrop_xexpression) {
        this.caltrop_xexpressions.add(caltrop_xexpression);
    }
    public caltrop_OutputAction getCaltrop_outputaction() {
        return caltrop_outputaction;
    }

    public void setCaltrop_outputaction(caltrop_OutputAction caltrop_outputaction) {
        this.caltrop_outputaction = caltrop_outputaction;
    }

}






import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETEdge  {

    private boolean controllable;





    private ecdarText_ETExpression ecdartext_etexpression;




    private List<ecdarText_ETExpression> ecdartext_etexpressions;




    private ecdarText_ETLocation ecdartext_etlocation;




    private ecdarText_ETLocation ecdartext_etlocation;


    public ecdarText_ETEdge(
        boolean controllable    ) {
        this.controllable = controllable;
        this.ecdartext_etexpressions = new ArrayList<>();
    }

    public ecdarText_ETEdge(
        boolean controllable        ArrayList<ecdarText_ETExpression> ecdartext_etexpressions    ) {
        this.controllable = controllable;
        this.ecdartext_etexpressions = ecdartext_etexpressions;
    }

    public boolean getControllable() {
        return controllable;
    }

    public void setControllable(boolean controllable) {
        this.controllable = controllable;
    }

    public ecdarText_ETExpression getEcdartext_etexpression() {
        return ecdartext_etexpression;
    }

    public void setEcdartext_etexpression(ecdarText_ETExpression ecdartext_etexpression) {
        this.ecdartext_etexpression = ecdartext_etexpression;
    }
    public List<ecdarText_ETExpression> getEcdartext_etexpressions() {
        return ecdartext_etexpressions;
    }

    public void addEcdartext_etexpression(Ecdartext_etexpression ecdartext_etexpression) {
        this.ecdartext_etexpressions.add(ecdartext_etexpression);
    }
    public ecdarText_ETLocation getEcdartext_etlocation() {
        return ecdartext_etlocation;
    }

    public void setEcdartext_etlocation(ecdarText_ETLocation ecdartext_etlocation) {
        this.ecdartext_etlocation = ecdartext_etlocation;
    }
    public ecdarText_ETLocation getEcdartext_etlocation() {
        return ecdartext_etlocation;
    }

    public void setEcdartext_etlocation(ecdarText_ETLocation ecdartext_etlocation) {
        this.ecdartext_etlocation = ecdartext_etlocation;
    }

}






import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETEdge  {

    private boolean controllable;





    private ecdarText_ETLocation ecdartext_etlocation;




    private ecdarText_ETLocation ecdartext_etlocation;




    private List<ecdarText_ETSelect> ecdartext_etselects;




    private ecdarText_ETExpression ecdartext_etexpression;




    private ecdarText_ETIO ecdartext_etio;




    private List<ecdarText_ETExpression> ecdartext_etexpressions;


    public ecdarText_ETEdge(
        boolean controllable    ) {
        this.controllable = controllable;
        this.ecdartext_etselects = new ArrayList<>();
        this.ecdartext_etexpressions = new ArrayList<>();
    }

    public ecdarText_ETEdge(
        boolean controllable        ArrayList<ecdarText_ETSelect> ecdartext_etselects,        ArrayList<ecdarText_ETExpression> ecdartext_etexpressions    ) {
        this.controllable = controllable;
        this.ecdartext_etselects = ecdartext_etselects;
        this.ecdartext_etexpressions = ecdartext_etexpressions;
    }

    public boolean getControllable() {
        return controllable;
    }

    public void setControllable(boolean controllable) {
        this.controllable = controllable;
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
    public List<ecdarText_ETSelect> getEcdartext_etselects() {
        return ecdartext_etselects;
    }

    public void addEcdartext_etselect(Ecdartext_etselect ecdartext_etselect) {
        this.ecdartext_etselects.add(ecdartext_etselect);
    }
    public ecdarText_ETExpression getEcdartext_etexpression() {
        return ecdartext_etexpression;
    }

    public void setEcdartext_etexpression(ecdarText_ETExpression ecdartext_etexpression) {
        this.ecdartext_etexpression = ecdartext_etexpression;
    }
    public ecdarText_ETIO getEcdartext_etio() {
        return ecdartext_etio;
    }

    public void setEcdartext_etio(ecdarText_ETIO ecdartext_etio) {
        this.ecdartext_etio = ecdartext_etio;
    }
    public List<ecdarText_ETExpression> getEcdartext_etexpressions() {
        return ecdartext_etexpressions;
    }

    public void addEcdartext_etexpression(Ecdartext_etexpression ecdartext_etexpression) {
        this.ecdartext_etexpressions.add(ecdartext_etexpression);
    }

}






import java.util.List;
import java.util.ArrayList;

public class esper2Maude_ComparisonOperator  {

    private String eq;
    private String le;
    private String lt;
    private String gt;
    private String neq;
    private String ge;





    private esper2Maude_FilterOperator esper2maude_filteroperator;


    public esper2Maude_ComparisonOperator(
        String eq,        String le,        String lt,        String gt,        String neq,        String ge    ) {
        this.eq = eq;
        this.le = le;
        this.lt = lt;
        this.gt = gt;
        this.neq = neq;
        this.ge = ge;
    }


    public String getEq() {
        return eq;
    }

    public void setEq(String eq) {
        this.eq = eq;
    }
    public String getLe() {
        return le;
    }

    public void setLe(String le) {
        this.le = le;
    }
    public String getLt() {
        return lt;
    }

    public void setLt(String lt) {
        this.lt = lt;
    }
    public String getGt() {
        return gt;
    }

    public void setGt(String gt) {
        this.gt = gt;
    }
    public String getNeq() {
        return neq;
    }

    public void setNeq(String neq) {
        this.neq = neq;
    }
    public String getGe() {
        return ge;
    }

    public void setGe(String ge) {
        this.ge = ge;
    }

    public esper2Maude_FilterOperator getEsper2maude_filteroperator() {
        return esper2maude_filteroperator;
    }

    public void setEsper2maude_filteroperator(esper2Maude_FilterOperator esper2maude_filteroperator) {
        this.esper2maude_filteroperator = esper2maude_filteroperator;
    }

}
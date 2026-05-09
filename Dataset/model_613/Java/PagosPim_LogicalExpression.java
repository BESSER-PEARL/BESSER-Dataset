





import java.util.List;
import java.util.ArrayList;

public class PagosPim_LogicalExpression  {

    private String conOper;
    private String logicalOperator;
    private String literal;





    private PagosPim_IfCondition pagospim_ifcondition;




    private PagosPim_LogicalExpression pagospim_logicalexpression;


    public PagosPim_LogicalExpression(
        String conOper,        String logicalOperator,        String literal    ) {
        this.conOper = conOper;
        this.logicalOperator = logicalOperator;
        this.literal = literal;
    }


    public String getConoper() {
        return conOper;
    }

    public void setConoper(String conOper) {
        this.conOper = conOper;
    }
    public String getLogicaloperator() {
        return logicalOperator;
    }

    public void setLogicaloperator(String logicalOperator) {
        this.logicalOperator = logicalOperator;
    }
    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }

    public PagosPim_IfCondition getPagospim_ifcondition() {
        return pagospim_ifcondition;
    }

    public void setPagospim_ifcondition(PagosPim_IfCondition pagospim_ifcondition) {
        this.pagospim_ifcondition = pagospim_ifcondition;
    }
    public PagosPim_LogicalExpression getPagospim_logicalexpression() {
        return pagospim_logicalexpression;
    }

    public void setPagospim_logicalexpression(PagosPim_LogicalExpression pagospim_logicalexpression) {
        this.pagospim_logicalexpression = pagospim_logicalexpression;
    }

}
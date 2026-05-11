





import java.util.List;
import java.util.ArrayList;

public class mpl_ComparisonExpression  {

    private String comparisonOperator;





    private mpl_Expression mpl_expression;




    private mpl_WhileLoop mpl_whileloop;




    private mpl_Expression mpl_expression;




    private mpl_IfStatement mpl_ifstatement;


    public mpl_ComparisonExpression(
        String comparisonOperator    ) {
        this.comparisonOperator = comparisonOperator;
    }


    public String getComparisonoperator() {
        return comparisonOperator;
    }

    public void setComparisonoperator(String comparisonOperator) {
        this.comparisonOperator = comparisonOperator;
    }

    public mpl_Expression getMpl_expression() {
        return mpl_expression;
    }

    public void setMpl_expression(mpl_Expression mpl_expression) {
        this.mpl_expression = mpl_expression;
    }
    public mpl_WhileLoop getMpl_whileloop() {
        return mpl_whileloop;
    }

    public void setMpl_whileloop(mpl_WhileLoop mpl_whileloop) {
        this.mpl_whileloop = mpl_whileloop;
    }
    public mpl_Expression getMpl_expression() {
        return mpl_expression;
    }

    public void setMpl_expression(mpl_Expression mpl_expression) {
        this.mpl_expression = mpl_expression;
    }
    public mpl_IfStatement getMpl_ifstatement() {
        return mpl_ifstatement;
    }

    public void setMpl_ifstatement(mpl_IfStatement mpl_ifstatement) {
        this.mpl_ifstatement = mpl_ifstatement;
    }

}






import java.util.List;
import java.util.ArrayList;

public class delphi_assignmentStmnt extends simpleStatement {

    private String operator;





    private delphi_expression delphi_expression;




    private delphi_designator delphi_designator;


    public delphi_assignmentStmnt(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public delphi_expression getDelphi_expression() {
        return delphi_expression;
    }

    public void setDelphi_expression(delphi_expression delphi_expression) {
        this.delphi_expression = delphi_expression;
    }
    public delphi_designator getDelphi_designator() {
        return delphi_designator;
    }

    public void setDelphi_designator(delphi_designator delphi_designator) {
        this.delphi_designator = delphi_designator;
    }

}
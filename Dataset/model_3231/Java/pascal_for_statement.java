





import java.util.List;
import java.util.ArrayList;

public class pascal_for_statement  {

    private String initID;





    private pascal_expression pascal_expression;




    private pascal_statement pascal_statement;




    private pascal_expression pascal_expression;




    private pascal_repetitive_statement pascal_repetitive_statement;


    public pascal_for_statement(
        String initID    ) {
        this.initID = initID;
    }


    public String getInitid() {
        return initID;
    }

    public void setInitid(String initID) {
        this.initID = initID;
    }

    public pascal_expression getPascal_expression() {
        return pascal_expression;
    }

    public void setPascal_expression(pascal_expression pascal_expression) {
        this.pascal_expression = pascal_expression;
    }
    public pascal_statement getPascal_statement() {
        return pascal_statement;
    }

    public void setPascal_statement(pascal_statement pascal_statement) {
        this.pascal_statement = pascal_statement;
    }
    public pascal_expression getPascal_expression() {
        return pascal_expression;
    }

    public void setPascal_expression(pascal_expression pascal_expression) {
        this.pascal_expression = pascal_expression;
    }
    public pascal_repetitive_statement getPascal_repetitive_statement() {
        return pascal_repetitive_statement;
    }

    public void setPascal_repetitive_statement(pascal_repetitive_statement pascal_repetitive_statement) {
        this.pascal_repetitive_statement = pascal_repetitive_statement;
    }

}
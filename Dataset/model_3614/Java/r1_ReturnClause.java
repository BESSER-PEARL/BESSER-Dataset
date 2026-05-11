





import java.util.List;
import java.util.ArrayList;

public class r1_ReturnClause extends Element {

    private String distinct;





    private r1_Expression r1_expression;




    private r1_Query r1_query;


    public r1_ReturnClause(
        String distinct    ) {
        super(
        );
        this.distinct = distinct;
    }


    public String getDistinct() {
        return distinct;
    }

    public void setDistinct(String distinct) {
        this.distinct = distinct;
    }

    public r1_Expression getR1_expression() {
        return r1_expression;
    }

    public void setR1_expression(r1_Expression r1_expression) {
        this.r1_expression = r1_expression;
    }
    public r1_Query getR1_query() {
        return r1_query;
    }

    public void setR1_query(r1_Query r1_query) {
        this.r1_query = r1_query;
    }

}
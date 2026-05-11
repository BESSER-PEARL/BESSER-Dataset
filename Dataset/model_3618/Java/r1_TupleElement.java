





import java.util.List;
import java.util.ArrayList;

public class r1_TupleElement  {

    private String name;





    private r1_Tuple r1_tuple;




    private r1_Expression r1_expression;


    public r1_TupleElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public r1_Tuple getR1_tuple() {
        return r1_tuple;
    }

    public void setR1_tuple(r1_Tuple r1_tuple) {
        this.r1_tuple = r1_tuple;
    }
    public r1_Expression getR1_expression() {
        return r1_expression;
    }

    public void setR1_expression(r1_Expression r1_expression) {
        this.r1_expression = r1_expression;
    }

}
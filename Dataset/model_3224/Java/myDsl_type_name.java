





import java.util.List;
import java.util.ArrayList;

public class myDsl_type_name extends postfix_expression {






    private myDsl_unary_expression mydsl_unary_expression;




    private myDsl_cast_expression mydsl_cast_expression;




    private myDsl_generic_association mydsl_generic_association;


    public myDsl_type_name(
    ) {
        super(
        );
    }



    public myDsl_unary_expression getMydsl_unary_expression() {
        return mydsl_unary_expression;
    }

    public void setMydsl_unary_expression(myDsl_unary_expression mydsl_unary_expression) {
        this.mydsl_unary_expression = mydsl_unary_expression;
    }
    public myDsl_cast_expression getMydsl_cast_expression() {
        return mydsl_cast_expression;
    }

    public void setMydsl_cast_expression(myDsl_cast_expression mydsl_cast_expression) {
        this.mydsl_cast_expression = mydsl_cast_expression;
    }
    public myDsl_generic_association getMydsl_generic_association() {
        return mydsl_generic_association;
    }

    public void setMydsl_generic_association(myDsl_generic_association mydsl_generic_association) {
        this.mydsl_generic_association = mydsl_generic_association;
    }

}
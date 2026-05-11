





import java.util.List;
import java.util.ArrayList;

public class myDsl_constant_expression  {






    private myDsl_static_assert_declaration mydsl_static_assert_declaration;




    private myDsl_conditional_expression mydsl_conditional_expression;


    public myDsl_constant_expression(
    ) {
    }



    public myDsl_static_assert_declaration getMydsl_static_assert_declaration() {
        return mydsl_static_assert_declaration;
    }

    public void setMydsl_static_assert_declaration(myDsl_static_assert_declaration mydsl_static_assert_declaration) {
        this.mydsl_static_assert_declaration = mydsl_static_assert_declaration;
    }
    public myDsl_conditional_expression getMydsl_conditional_expression() {
        return mydsl_conditional_expression;
    }

    public void setMydsl_conditional_expression(myDsl_conditional_expression mydsl_conditional_expression) {
        this.mydsl_conditional_expression = mydsl_conditional_expression;
    }

}
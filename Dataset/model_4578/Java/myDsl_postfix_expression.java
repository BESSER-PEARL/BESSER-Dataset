





import java.util.List;
import java.util.ArrayList;

public class myDsl_postfix_expression extends unary_expression {






    private myDsl_initializer_list mydsl_initializer_list;


    public myDsl_postfix_expression(
    ) {
        super(
        );
    }



    public myDsl_initializer_list getMydsl_initializer_list() {
        return mydsl_initializer_list;
    }

    public void setMydsl_initializer_list(myDsl_initializer_list mydsl_initializer_list) {
        this.mydsl_initializer_list = mydsl_initializer_list;
    }

}
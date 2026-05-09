





import java.util.List;
import java.util.ArrayList;

public class dsl_EObject  {






    private dsl_CastExpression dsl_castexpression;




    private dsl_PrimaryExpression dsl_primaryexpression;


    public dsl_EObject(
    ) {
    }



    public dsl_CastExpression getDsl_castexpression() {
        return dsl_castexpression;
    }

    public void setDsl_castexpression(dsl_CastExpression dsl_castexpression) {
        this.dsl_castexpression = dsl_castexpression;
    }
    public dsl_PrimaryExpression getDsl_primaryexpression() {
        return dsl_primaryexpression;
    }

    public void setDsl_primaryexpression(dsl_PrimaryExpression dsl_primaryexpression) {
        this.dsl_primaryexpression = dsl_primaryexpression;
    }

}
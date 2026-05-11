





import java.util.List;
import java.util.ArrayList;

public class alf_BooleanNegationExpression extends NonPostfixNonCastUnaryExpression, CastCompletion {






    private alf_UnaryExpression alf_unaryexpression;


    public alf_BooleanNegationExpression(
    ) {
        super(
        );
    }



    public alf_UnaryExpression getAlf_unaryexpression() {
        return alf_unaryexpression;
    }

    public void setAlf_unaryexpression(alf_UnaryExpression alf_unaryexpression) {
        this.alf_unaryexpression = alf_unaryexpression;
    }

}
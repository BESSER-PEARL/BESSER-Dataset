





import java.util.List;
import java.util.ArrayList;

public class dsl_BooleanLiteral  {

    private String truthiness;





    private dsl_Literal dsl_literal;


    public dsl_BooleanLiteral(
        String truthiness    ) {
        this.truthiness = truthiness;
    }


    public String getTruthiness() {
        return truthiness;
    }

    public void setTruthiness(String truthiness) {
        this.truthiness = truthiness;
    }

    public dsl_Literal getDsl_literal() {
        return dsl_literal;
    }

    public void setDsl_literal(dsl_Literal dsl_literal) {
        this.dsl_literal = dsl_literal;
    }

}
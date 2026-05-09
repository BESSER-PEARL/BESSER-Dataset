





import java.util.List;
import java.util.ArrayList;

public class dsl_Literal  {

    private String nullLit;
    private String stringLit;
    private String charLit;





    private dsl_CastLookahead dsl_castlookahead;


    public dsl_Literal(
        String nullLit,        String stringLit,        String charLit    ) {
        this.nullLit = nullLit;
        this.stringLit = stringLit;
        this.charLit = charLit;
    }


    public String getNulllit() {
        return nullLit;
    }

    public void setNulllit(String nullLit) {
        this.nullLit = nullLit;
    }
    public String getStringlit() {
        return stringLit;
    }

    public void setStringlit(String stringLit) {
        this.stringLit = stringLit;
    }
    public String getCharlit() {
        return charLit;
    }

    public void setCharlit(String charLit) {
        this.charLit = charLit;
    }

    public dsl_CastLookahead getDsl_castlookahead() {
        return dsl_castlookahead;
    }

    public void setDsl_castlookahead(dsl_CastLookahead dsl_castlookahead) {
        this.dsl_castlookahead = dsl_castlookahead;
    }

}
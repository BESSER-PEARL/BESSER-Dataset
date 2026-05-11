





import java.util.List;
import java.util.ArrayList;

public class netModel_NumericLiteral extends Literal {

    private String literal;



    public netModel_NumericLiteral(
        String literal    ) {
        super(
        );
        this.literal = literal;
    }


    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }


}
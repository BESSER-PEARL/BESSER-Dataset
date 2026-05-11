





import java.util.List;
import java.util.ArrayList;

public class netModel_BooleanLiteral extends Literal {

    private String literal;



    public netModel_BooleanLiteral(
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
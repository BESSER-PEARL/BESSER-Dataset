





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_NullLiteral extends LiteralValue {

    private String literal;



    public sqliteModel_NullLiteral(
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
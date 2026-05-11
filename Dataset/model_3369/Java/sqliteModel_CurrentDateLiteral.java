





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_CurrentDateLiteral extends LiteralValue {

    private String literal;



    public sqliteModel_CurrentDateLiteral(
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
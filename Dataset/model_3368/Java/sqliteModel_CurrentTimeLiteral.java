





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_CurrentTimeLiteral extends LiteralValue {

    private String literal;



    public sqliteModel_CurrentTimeLiteral(
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






import java.util.List;
import java.util.ArrayList;

public class sqliteModel_NumericLiteral extends LiteralValue {

    private String number;



    public sqliteModel_NumericLiteral(
        String number    ) {
        super(
        );
        this.number = number;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }


}
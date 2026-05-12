





import java.util.List;
import java.util.ArrayList;

public class sparql_DECIMAL extends NumericLiteral {

    private String decimal;



    public sparql_DECIMAL(
        String decimal    ) {
        super(
        );
        this.decimal = decimal;
    }


    public String getDecimal() {
        return decimal;
    }

    public void setDecimal(String decimal) {
        this.decimal = decimal;
    }


}
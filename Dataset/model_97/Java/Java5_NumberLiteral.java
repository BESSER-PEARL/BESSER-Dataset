





import java.util.List;
import java.util.ArrayList;

public class Java5_NumberLiteral extends Expression {

    private String tokenValue;



    public Java5_NumberLiteral(
        String tokenValue    ) {
        super(
        );
        this.tokenValue = tokenValue;
    }


    public String getTokenvalue() {
        return tokenValue;
    }

    public void setTokenvalue(String tokenValue) {
        this.tokenValue = tokenValue;
    }


}
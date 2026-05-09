





import java.util.List;
import java.util.ArrayList;

public class java__NumberLiteral extends Expression {

    private String tokenValue;



    public java__NumberLiteral(
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
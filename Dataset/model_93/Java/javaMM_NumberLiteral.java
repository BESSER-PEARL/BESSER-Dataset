





import java.util.List;
import java.util.ArrayList;

public class javaMM_NumberLiteral extends Expression {

    private String tokenValue;



    public javaMM_NumberLiteral(
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
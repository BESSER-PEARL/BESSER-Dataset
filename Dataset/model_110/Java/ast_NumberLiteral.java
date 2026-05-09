





import java.util.List;
import java.util.ArrayList;

public class ast_NumberLiteral extends Expression {

    private String token;



    public ast_NumberLiteral(
        String token    ) {
        super(
        );
        this.token = token;
    }


    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }


}
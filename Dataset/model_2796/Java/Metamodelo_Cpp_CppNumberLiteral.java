





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppNumberLiteral extends CppExpression {

    private String token;



    public Metamodelo_Cpp_CppNumberLiteral(
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
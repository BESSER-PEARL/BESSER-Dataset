





import java.util.List;
import java.util.ArrayList;

public class xtextTest_MyTokens  {

    private String token;
    private String string;
    private int count;





    private xtextTest_Tokens xtexttest_tokens;


    public xtextTest_MyTokens(
        String token,        String string,        int count    ) {
        this.token = token;
        this.string = string;
        this.count = count;
    }


    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }
    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public xtextTest_Tokens getXtexttest_tokens() {
        return xtexttest_tokens;
    }

    public void setXtexttest_tokens(xtextTest_Tokens xtexttest_tokens) {
        this.xtexttest_tokens = xtexttest_tokens;
    }

}
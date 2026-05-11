





import java.util.List;
import java.util.ArrayList;

public class test_OAuth2 extends Authorization {

    private String token;



    public test_OAuth2(
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
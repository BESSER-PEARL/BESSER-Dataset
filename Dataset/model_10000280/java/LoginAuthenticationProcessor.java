





import java.util.List;
import java.util.ArrayList;

public class LoginAuthenticationProcessor  {

    private String UserPassWord;
    private boolean Authentication_Result;
    private String UserID;



    public LoginAuthenticationProcessor(
        String UserPassWord,        boolean Authentication_Result,        String UserID    ) {
        this.UserPassWord = UserPassWord;
        this.Authentication_Result = Authentication_Result;
        this.UserID = UserID;
    }


    public String getUserpassword() {
        return UserPassWord;
    }

    public void setUserpassword(String UserPassWord) {
        this.UserPassWord = UserPassWord;
    }
    public boolean getAuthentication_result() {
        return Authentication_Result;
    }

    public void setAuthentication_result(boolean Authentication_Result) {
        this.Authentication_Result = Authentication_Result;
    }
    public String getUserid() {
        return UserID;
    }

    public void setUserid(String UserID) {
        this.UserID = UserID;
    }


}
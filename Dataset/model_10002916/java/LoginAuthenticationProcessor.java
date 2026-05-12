





import java.util.List;
import java.util.ArrayList;

public class LoginAuthenticationProcessor  {

    private String UserPassWord;
    private String UserID;
    private boolean Authentication_Result;



    public LoginAuthenticationProcessor(
        String UserPassWord,        String UserID,        boolean Authentication_Result    ) {
        this.UserPassWord = UserPassWord;
        this.UserID = UserID;
        this.Authentication_Result = Authentication_Result;
    }


    public String getUserpassword() {
        return UserPassWord;
    }

    public void setUserpassword(String UserPassWord) {
        this.UserPassWord = UserPassWord;
    }
    public String getUserid() {
        return UserID;
    }

    public void setUserid(String UserID) {
        this.UserID = UserID;
    }
    public boolean getAuthentication_result() {
        return Authentication_Result;
    }

    public void setAuthentication_result(boolean Authentication_Result) {
        this.Authentication_Result = Authentication_Result;
    }


}
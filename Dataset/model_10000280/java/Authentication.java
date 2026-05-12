





import java.util.List;
import java.util.ArrayList;

public class Authentication  {

    private boolean Authentication_Result;
    private int AuthenticationType;
    private String UserEmail;
    private String UserPassWord;
    private String UserPassWord1;
    private String UserID;



    public Authentication(
        boolean Authentication_Result,        int AuthenticationType,        String UserEmail,        String UserPassWord,        String UserPassWord1,        String UserID    ) {
        this.Authentication_Result = Authentication_Result;
        this.AuthenticationType = AuthenticationType;
        this.UserEmail = UserEmail;
        this.UserPassWord = UserPassWord;
        this.UserPassWord1 = UserPassWord1;
        this.UserID = UserID;
    }


    public boolean getAuthentication_result() {
        return Authentication_Result;
    }

    public void setAuthentication_result(boolean Authentication_Result) {
        this.Authentication_Result = Authentication_Result;
    }
    public int getAuthenticationtype() {
        return AuthenticationType;
    }

    public void setAuthenticationtype(int AuthenticationType) {
        this.AuthenticationType = AuthenticationType;
    }
    public String getUseremail() {
        return UserEmail;
    }

    public void setUseremail(String UserEmail) {
        this.UserEmail = UserEmail;
    }
    public String getUserpassword() {
        return UserPassWord;
    }

    public void setUserpassword(String UserPassWord) {
        this.UserPassWord = UserPassWord;
    }
    public String getUserpassword1() {
        return UserPassWord1;
    }

    public void setUserpassword1(String UserPassWord1) {
        this.UserPassWord1 = UserPassWord1;
    }
    public String getUserid() {
        return UserID;
    }

    public void setUserid(String UserID) {
        this.UserID = UserID;
    }


}
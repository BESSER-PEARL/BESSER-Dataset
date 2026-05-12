





import java.util.List;
import java.util.ArrayList;

public class RequestOTPAuthentication  {

    private String UserEmail;
    private String UserID;



    public RequestOTPAuthentication(
        String UserEmail,        String UserID    ) {
        this.UserEmail = UserEmail;
        this.UserID = UserID;
    }


    public String getUseremail() {
        return UserEmail;
    }

    public void setUseremail(String UserEmail) {
        this.UserEmail = UserEmail;
    }
    public String getUserid() {
        return UserID;
    }

    public void setUserid(String UserID) {
        this.UserID = UserID;
    }


}
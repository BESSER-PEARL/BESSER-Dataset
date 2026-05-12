





import java.util.List;
import java.util.ArrayList;

public class RequestOTPAuthentication  {

    private String UserID;
    private String UserEmail;



    public RequestOTPAuthentication(
        String UserID,        String UserEmail    ) {
        this.UserID = UserID;
        this.UserEmail = UserEmail;
    }


    public String getUserid() {
        return UserID;
    }

    public void setUserid(String UserID) {
        this.UserID = UserID;
    }
    public String getUseremail() {
        return UserEmail;
    }

    public void setUseremail(String UserEmail) {
        this.UserEmail = UserEmail;
    }


}
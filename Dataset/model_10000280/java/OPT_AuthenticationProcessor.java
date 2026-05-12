





import java.util.List;
import java.util.ArrayList;

public class OPT_AuthenticationProcessor  {

    private boolean Authentication_Result;
    private String UserEmail;



    public OPT_AuthenticationProcessor(
        boolean Authentication_Result,        String UserEmail    ) {
        this.Authentication_Result = Authentication_Result;
        this.UserEmail = UserEmail;
    }


    public boolean getAuthentication_result() {
        return Authentication_Result;
    }

    public void setAuthentication_result(boolean Authentication_Result) {
        this.Authentication_Result = Authentication_Result;
    }
    public String getUseremail() {
        return UserEmail;
    }

    public void setUseremail(String UserEmail) {
        this.UserEmail = UserEmail;
    }


}
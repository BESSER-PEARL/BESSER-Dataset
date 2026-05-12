





import java.util.List;
import java.util.ArrayList;

public class D_B_details  {

    private String session_out;
    private String logged_in;



    public D_B_details(
        String session_out,        String logged_in    ) {
        this.session_out = session_out;
        this.logged_in = logged_in;
    }


    public String getSession_out() {
        return session_out;
    }

    public void setSession_out(String session_out) {
        this.session_out = session_out;
    }
    public String getLogged_in() {
        return logged_in;
    }

    public void setLogged_in(String logged_in) {
        this.logged_in = logged_in;
    }


}
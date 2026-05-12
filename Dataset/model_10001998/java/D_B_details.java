





import java.util.List;
import java.util.ArrayList;

public class D_B_details  {

    private String logged_in;
    private String session_out;



    public D_B_details(
        String logged_in,        String session_out    ) {
        this.logged_in = logged_in;
        this.session_out = session_out;
    }


    public String getLogged_in() {
        return logged_in;
    }

    public void setLogged_in(String logged_in) {
        this.logged_in = logged_in;
    }
    public String getSession_out() {
        return session_out;
    }

    public void setSession_out(String session_out) {
        this.session_out = session_out;
    }


}
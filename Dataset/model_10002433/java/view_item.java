





import java.util.List;
import java.util.ArrayList;

public class view_item  {

    private String ticket_id_;





    private Login login;


    public view_item(
        String ticket_id_    ) {
        this.ticket_id_ = ticket_id_;
    }


    public String getTicket_id_() {
        return ticket_id_;
    }

    public void setTicket_id_(String ticket_id_) {
        this.ticket_id_ = ticket_id_;
    }

    public Login getLogin() {
        return login;
    }

    public void setLogin(Login login) {
        this.login = login;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Cancle  {

    private String ticket_id_;
    private String user_id_;





    private Book_a_ticek book_a_ticek;


    public Cancle(
        String ticket_id_,        String user_id_    ) {
        this.ticket_id_ = ticket_id_;
        this.user_id_ = user_id_;
    }


    public String getTicket_id_() {
        return ticket_id_;
    }

    public void setTicket_id_(String ticket_id_) {
        this.ticket_id_ = ticket_id_;
    }
    public String getUser_id_() {
        return user_id_;
    }

    public void setUser_id_(String user_id_) {
        this.user_id_ = user_id_;
    }

    public Book_a_ticek getBook_a_ticek() {
        return book_a_ticek;
    }

    public void setBook_a_ticek(Book_a_ticek book_a_ticek) {
        this.book_a_ticek = book_a_ticek;
    }

}
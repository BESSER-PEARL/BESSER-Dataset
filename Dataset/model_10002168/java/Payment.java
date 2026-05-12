





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private None price;
    private None date;
    private None username;
    private None Ticketnumber;
    private String Method;





    private Ticket ticket;


    public Payment(
        None price,        None date,        None username,        None Ticketnumber,        String Method    ) {
        this.price = price;
        this.date = date;
        this.username = username;
        this.Ticketnumber = Ticketnumber;
        this.Method = Method;
    }


    public None getPrice() {
        return price;
    }

    public void setPrice(None price) {
        this.price = price;
    }
    public None getDate() {
        return date;
    }

    public void setDate(None date) {
        this.date = date;
    }
    public None getUsername() {
        return username;
    }

    public void setUsername(None username) {
        this.username = username;
    }
    public None getTicketnumber() {
        return Ticketnumber;
    }

    public void setTicketnumber(None Ticketnumber) {
        this.Ticketnumber = Ticketnumber;
    }
    public String getMethod() {
        return Method;
    }

    public void setMethod(String Method) {
        this.Method = Method;
    }

    public Ticket getTicket() {
        return ticket;
    }

    public void setTicket(Ticket ticket) {
        this.ticket = ticket;
    }

}
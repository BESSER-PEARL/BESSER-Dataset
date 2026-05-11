





import java.util.List;
import java.util.ArrayList;

public class pokerleague_Player extends IdentifiableEntity {

    private boolean active;
    private String nick;
    private String lastName;
    private String firstName;
    private String emailAddress;



    public pokerleague_Player(
        boolean active,        String nick,        String lastName,        String firstName,        String emailAddress    ) {
        super(
        );
        this.active = active;
        this.nick = nick;
        this.lastName = lastName;
        this.firstName = firstName;
        this.emailAddress = emailAddress;
    }


    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public String getNick() {
        return nick;
    }

    public void setNick(String nick) {
        this.nick = nick;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }


}
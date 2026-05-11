





import java.util.List;
import java.util.ArrayList;

public class pokerleague_Player extends IdentifiableEntity {

    private String emailAddress;
    private String lastName;
    private String nick;
    private boolean active;
    private String firstName;



    public pokerleague_Player(
        String emailAddress,        String lastName,        String nick,        boolean active,        String firstName    ) {
        super(
        );
        this.emailAddress = emailAddress;
        this.lastName = lastName;
        this.nick = nick;
        this.active = active;
        this.firstName = firstName;
    }


    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getNick() {
        return nick;
    }

    public void setNick(String nick) {
        this.nick = nick;
    }
    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }


}
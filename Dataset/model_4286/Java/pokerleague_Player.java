





import java.util.List;
import java.util.ArrayList;

public class pokerleague_Player extends IdentifiableEntity {

    private boolean active;
    private String lastName;
    private String emailAddress;
    private String nick;
    private String firstName;





    private pokerleague_Invitation pokerleague_invitation;


    public pokerleague_Player(
        boolean active,        String lastName,        String emailAddress,        String nick,        String firstName    ) {
        super(
        );
        this.active = active;
        this.lastName = lastName;
        this.emailAddress = emailAddress;
        this.nick = nick;
        this.firstName = firstName;
    }


    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }
    public String getNick() {
        return nick;
    }

    public void setNick(String nick) {
        this.nick = nick;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public pokerleague_Invitation getPokerleague_invitation() {
        return pokerleague_invitation;
    }

    public void setPokerleague_invitation(pokerleague_Invitation pokerleague_invitation) {
        this.pokerleague_invitation = pokerleague_invitation;
    }

}
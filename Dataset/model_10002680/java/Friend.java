





import java.util.List;
import java.util.ArrayList;

public class Friend  {

    private String friend____;
    private boolean acceptornot;





    private User user;


    public Friend(
        String friend____,        boolean acceptornot    ) {
        this.friend____ = friend____;
        this.acceptornot = acceptornot;
    }


    public String getFriend____() {
        return friend____;
    }

    public void setFriend____(String friend____) {
        this.friend____ = friend____;
    }
    public boolean getAcceptornot() {
        return acceptornot;
    }

    public void setAcceptornot(boolean acceptornot) {
        this.acceptornot = acceptornot;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}
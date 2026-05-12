





import java.util.List;
import java.util.ArrayList;

public class HomePage  {

    private boolean likeorunlike;
    private String __status;
    private String __friendStatus;





    private User user;


    public HomePage(
        boolean likeorunlike,        String __status,        String __friendStatus    ) {
        this.likeorunlike = likeorunlike;
        this.__status = __status;
        this.__friendStatus = __friendStatus;
    }


    public boolean getLikeorunlike() {
        return likeorunlike;
    }

    public void setLikeorunlike(boolean likeorunlike) {
        this.likeorunlike = likeorunlike;
    }
    public String get__status() {
        return __status;
    }

    public void set__status(String __status) {
        this.__status = __status;
    }
    public String get__friendstatus() {
        return __friendStatus;
    }

    public void set__friendstatus(String __friendStatus) {
        this.__friendStatus = __friendStatus;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}
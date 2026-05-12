





import java.util.List;
import java.util.ArrayList;

public class HomePage  {

    private String __status;
    private boolean likeorunlike;
    private String __friendStatus;





    private User user;


    public HomePage(
        String __status,        boolean likeorunlike,        String __friendStatus    ) {
        this.__status = __status;
        this.likeorunlike = likeorunlike;
        this.__friendStatus = __friendStatus;
    }


    public String get__status() {
        return __status;
    }

    public void set__status(String __status) {
        this.__status = __status;
    }
    public boolean getLikeorunlike() {
        return likeorunlike;
    }

    public void setLikeorunlike(boolean likeorunlike) {
        this.likeorunlike = likeorunlike;
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
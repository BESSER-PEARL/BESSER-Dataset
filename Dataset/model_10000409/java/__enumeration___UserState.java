





import java.util.List;
import java.util.ArrayList;

public class __enumeration___UserState  {

    private String banned;
    private String new;
    private String blocked;
    private String active;



    public __enumeration___UserState(
        String banned,        String new,        String blocked,        String active    ) {
        this.banned = banned;
        this.new = new;
        this.blocked = blocked;
        this.active = active;
    }


    public String getBanned() {
        return banned;
    }

    public void setBanned(String banned) {
        this.banned = banned;
    }
    public String getNew() {
        return new;
    }

    public void setNew(String new) {
        this.new = new;
    }
    public String getBlocked() {
        return blocked;
    }

    public void setBlocked(String blocked) {
        this.blocked = blocked;
    }
    public String getActive() {
        return active;
    }

    public void setActive(String active) {
        this.active = active;
    }


}
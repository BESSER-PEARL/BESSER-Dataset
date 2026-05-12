





import java.util.List;
import java.util.ArrayList;

public class __enumeration___UserState  {

    private String banned;
    private String active;
    private String blocked;
    private String new;



    public __enumeration___UserState(
        String banned,        String active,        String blocked,        String new    ) {
        this.banned = banned;
        this.active = active;
        this.blocked = blocked;
        this.new = new;
    }


    public String getBanned() {
        return banned;
    }

    public void setBanned(String banned) {
        this.banned = banned;
    }
    public String getActive() {
        return active;
    }

    public void setActive(String active) {
        this.active = active;
    }
    public String getBlocked() {
        return blocked;
    }

    public void setBlocked(String blocked) {
        this.blocked = blocked;
    }
    public String getNew() {
        return new;
    }

    public void setNew(String new) {
        this.new = new;
    }


}
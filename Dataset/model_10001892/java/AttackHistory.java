





import java.util.List;
import java.util.ArrayList;

public class AttackHistory  {

    private boolean auto;
    private int date;
    private String target;





    private User user;


    public AttackHistory(
        boolean auto,        int date,        String target    ) {
        this.auto = auto;
        this.date = date;
        this.target = target;
    }


    public boolean getAuto() {
        return auto;
    }

    public void setAuto(boolean auto) {
        this.auto = auto;
    }
    public int getDate() {
        return date;
    }

    public void setDate(int date) {
        this.date = date;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}
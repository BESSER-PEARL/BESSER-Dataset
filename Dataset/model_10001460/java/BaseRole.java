





import java.util.List;
import java.util.ArrayList;

public class BaseRole  {

    private None night_action;
    private None appear_as;
    private None wins_with;
    private None role;



    public BaseRole(
        None night_action,        None appear_as,        None wins_with,        None role    ) {
        this.night_action = night_action;
        this.appear_as = appear_as;
        this.wins_with = wins_with;
        this.role = role;
    }


    public None getNight_action() {
        return night_action;
    }

    public void setNight_action(None night_action) {
        this.night_action = night_action;
    }
    public None getAppear_as() {
        return appear_as;
    }

    public void setAppear_as(None appear_as) {
        this.appear_as = appear_as;
    }
    public None getWins_with() {
        return wins_with;
    }

    public void setWins_with(None wins_with) {
        this.wins_with = wins_with;
    }
    public None getRole() {
        return role;
    }

    public void setRole(None role) {
        this.role = role;
    }


}
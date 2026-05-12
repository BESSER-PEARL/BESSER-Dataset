





import java.util.List;
import java.util.ArrayList;

public class Train  {

    private String myCoach;
    private String myEngine;



    public Train(
        String myCoach,        String myEngine    ) {
        this.myCoach = myCoach;
        this.myEngine = myEngine;
    }


    public String getMycoach() {
        return myCoach;
    }

    public void setMycoach(String myCoach) {
        this.myCoach = myCoach;
    }
    public String getMyengine() {
        return myEngine;
    }

    public void setMyengine(String myEngine) {
        this.myEngine = myEngine;
    }


}
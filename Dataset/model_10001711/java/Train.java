





import java.util.List;
import java.util.ArrayList;

public class Train  {

    private String myEngine;
    private String myCoach;



    public Train(
        String myEngine,        String myCoach    ) {
        this.myEngine = myEngine;
        this.myCoach = myCoach;
    }


    public String getMyengine() {
        return myEngine;
    }

    public void setMyengine(String myEngine) {
        this.myEngine = myEngine;
    }
    public String getMycoach() {
        return myCoach;
    }

    public void setMycoach(String myCoach) {
        this.myCoach = myCoach;
    }


}
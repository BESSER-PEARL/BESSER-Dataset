





import java.util.List;
import java.util.ArrayList;

public class effbdpattern_Condition  {

    private String name;





    private effbdpattern_Context effbdpattern_context;




    private effbdpattern_Force effbdpattern_force;


    public effbdpattern_Condition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public effbdpattern_Context getEffbdpattern_context() {
        return effbdpattern_context;
    }

    public void setEffbdpattern_context(effbdpattern_Context effbdpattern_context) {
        this.effbdpattern_context = effbdpattern_context;
    }
    public effbdpattern_Force getEffbdpattern_force() {
        return effbdpattern_force;
    }

    public void setEffbdpattern_force(effbdpattern_Force effbdpattern_force) {
        this.effbdpattern_force = effbdpattern_force;
    }

}
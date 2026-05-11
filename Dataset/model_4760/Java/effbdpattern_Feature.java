





import java.util.List;
import java.util.ArrayList;

public class effbdpattern_Feature  {

    private String name;
    private String description;





    private effbdpattern_Problem effbdpattern_problem;




    private effbdpattern_Impact effbdpattern_impact;


    public effbdpattern_Feature(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public effbdpattern_Problem getEffbdpattern_problem() {
        return effbdpattern_problem;
    }

    public void setEffbdpattern_problem(effbdpattern_Problem effbdpattern_problem) {
        this.effbdpattern_problem = effbdpattern_problem;
    }
    public effbdpattern_Impact getEffbdpattern_impact() {
        return effbdpattern_impact;
    }

    public void setEffbdpattern_impact(effbdpattern_Impact effbdpattern_impact) {
        this.effbdpattern_impact = effbdpattern_impact;
    }

}
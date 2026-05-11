





import java.util.List;
import java.util.ArrayList;

public class gradingsystem_Grade  {

    private int requiredPoints;
    private String name;





    private gradingsystem_GradingScheme gradingsystem_gradingscheme;




    private gradingsystem_GradingScheme gradingsystem_gradingscheme;


    public gradingsystem_Grade(
        int requiredPoints,        String name    ) {
        this.requiredPoints = requiredPoints;
        this.name = name;
    }


    public int getRequiredpoints() {
        return requiredPoints;
    }

    public void setRequiredpoints(int requiredPoints) {
        this.requiredPoints = requiredPoints;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gradingsystem_GradingScheme getGradingsystem_gradingscheme() {
        return gradingsystem_gradingscheme;
    }

    public void setGradingsystem_gradingscheme(gradingsystem_GradingScheme gradingsystem_gradingscheme) {
        this.gradingsystem_gradingscheme = gradingsystem_gradingscheme;
    }
    public gradingsystem_GradingScheme getGradingsystem_gradingscheme() {
        return gradingsystem_gradingscheme;
    }

    public void setGradingsystem_gradingscheme(gradingsystem_GradingScheme gradingsystem_gradingscheme) {
        this.gradingsystem_gradingscheme = gradingsystem_gradingscheme;
    }

}
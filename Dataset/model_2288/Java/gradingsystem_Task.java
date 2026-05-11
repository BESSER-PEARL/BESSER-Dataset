





import java.util.List;
import java.util.ArrayList;

public class gradingsystem_Task  {

    private String name;





    private gradingsystem_Grading gradingsystem_grading;


    public gradingsystem_Task(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gradingsystem_Grading getGradingsystem_grading() {
        return gradingsystem_grading;
    }

    public void setGradingsystem_grading(gradingsystem_Grading gradingsystem_grading) {
        this.gradingsystem_grading = gradingsystem_grading;
    }

}
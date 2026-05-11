





import java.util.List;
import java.util.ArrayList;

public class gradingsystem_Course  {

    private String name;





    private gradingsystem_GradingSystem gradingsystem_gradingsystem;


    public gradingsystem_Course(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gradingsystem_GradingSystem getGradingsystem_gradingsystem() {
        return gradingsystem_gradingsystem;
    }

    public void setGradingsystem_gradingsystem(gradingsystem_GradingSystem gradingsystem_gradingsystem) {
        this.gradingsystem_gradingsystem = gradingsystem_gradingsystem;
    }

}






import java.util.List;
import java.util.ArrayList;

public class raspirover_RoverProgram  {

    private String name;





    private raspirover_Project raspirover_project;


    public raspirover_RoverProgram(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public raspirover_Project getRaspirover_project() {
        return raspirover_project;
    }

    public void setRaspirover_project(raspirover_Project raspirover_project) {
        this.raspirover_project = raspirover_project;
    }

}
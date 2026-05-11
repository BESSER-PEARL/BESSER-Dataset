





import java.util.List;
import java.util.ArrayList;

public class solution_Entity  {

    private String name;





    private solution_WebApplication solution_webapplication;


    public solution_Entity(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public solution_WebApplication getSolution_webapplication() {
        return solution_webapplication;
    }

    public void setSolution_webapplication(solution_WebApplication solution_webapplication) {
        this.solution_webapplication = solution_webapplication;
    }

}
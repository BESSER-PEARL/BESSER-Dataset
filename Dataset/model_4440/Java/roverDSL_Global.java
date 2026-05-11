





import java.util.List;
import java.util.ArrayList;

public class roverDSL_Global  {

    private String name;





    private roverDSL_Robot roverdsl_robot;


    public roverDSL_Global(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public roverDSL_Robot getRoverdsl_robot() {
        return roverdsl_robot;
    }

    public void setRoverdsl_robot(roverDSL_Robot roverdsl_robot) {
        this.roverdsl_robot = roverdsl_robot;
    }

}
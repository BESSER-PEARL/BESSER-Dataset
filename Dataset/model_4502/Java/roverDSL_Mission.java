





import java.util.List;
import java.util.ArrayList;

public class roverDSL_Mission  {

    private String id;





    private roverDSL_Robot roverdsl_robot;


    public roverDSL_Mission(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public roverDSL_Robot getRoverdsl_robot() {
        return roverdsl_robot;
    }

    public void setRoverdsl_robot(roverDSL_Robot roverdsl_robot) {
        this.roverdsl_robot = roverdsl_robot;
    }

}
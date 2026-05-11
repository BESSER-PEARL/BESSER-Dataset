





import java.util.List;
import java.util.ArrayList;

public class roverDSL_Implementation  {






    private roverDSL_Robot roverdsl_robot;




    private roverDSL_BehaviorName roverdsl_behaviorname;




    private roverDSL_ValueExpression roverdsl_valueexpression;


    public roverDSL_Implementation(
    ) {
    }



    public roverDSL_Robot getRoverdsl_robot() {
        return roverdsl_robot;
    }

    public void setRoverdsl_robot(roverDSL_Robot roverdsl_robot) {
        this.roverdsl_robot = roverdsl_robot;
    }
    public roverDSL_BehaviorName getRoverdsl_behaviorname() {
        return roverdsl_behaviorname;
    }

    public void setRoverdsl_behaviorname(roverDSL_BehaviorName roverdsl_behaviorname) {
        this.roverdsl_behaviorname = roverdsl_behaviorname;
    }
    public roverDSL_ValueExpression getRoverdsl_valueexpression() {
        return roverdsl_valueexpression;
    }

    public void setRoverdsl_valueexpression(roverDSL_ValueExpression roverdsl_valueexpression) {
        this.roverdsl_valueexpression = roverdsl_valueexpression;
    }

}






import java.util.List;
import java.util.ArrayList;

public class roverDSL_SAccelerationAction extends Action {






    private roverDSL_ValueExpression roverdsl_valueexpression;




    private roverDSL_Motor roverdsl_motor;


    public roverDSL_SAccelerationAction(
    ) {
        super(
        );
    }



    public roverDSL_ValueExpression getRoverdsl_valueexpression() {
        return roverdsl_valueexpression;
    }

    public void setRoverdsl_valueexpression(roverDSL_ValueExpression roverdsl_valueexpression) {
        this.roverdsl_valueexpression = roverdsl_valueexpression;
    }
    public roverDSL_Motor getRoverdsl_motor() {
        return roverdsl_motor;
    }

    public void setRoverdsl_motor(roverDSL_Motor roverdsl_motor) {
        this.roverdsl_motor = roverdsl_motor;
    }

}
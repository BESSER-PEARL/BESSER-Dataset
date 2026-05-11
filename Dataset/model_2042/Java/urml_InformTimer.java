





import java.util.List;
import java.util.ArrayList;

public class urml_InformTimer extends StatementOperation, Statement {






    private urml_Expression urml_expression;




    private urml_TimerPort urml_timerport;


    public urml_InformTimer(
    ) {
        super(
        );
    }



    public urml_Expression getUrml_expression() {
        return urml_expression;
    }

    public void setUrml_expression(urml_Expression urml_expression) {
        this.urml_expression = urml_expression;
    }
    public urml_TimerPort getUrml_timerport() {
        return urml_timerport;
    }

    public void setUrml_timerport(urml_TimerPort urml_timerport) {
        this.urml_timerport = urml_timerport;
    }

}
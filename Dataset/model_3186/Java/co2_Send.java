





import java.util.List;
import java.util.ArrayList;

public class co2_Send extends SendGroup {






    private co2_VariableDeclaration co2_variabledeclaration;




    private co2_Expression co2_expression;




    private co2_Process co2_process;




    private co2_IntAction co2_intaction;


    public co2_Send(
    ) {
        super(
        );
    }



    public co2_VariableDeclaration getCo2_variabledeclaration() {
        return co2_variabledeclaration;
    }

    public void setCo2_variabledeclaration(co2_VariableDeclaration co2_variabledeclaration) {
        this.co2_variabledeclaration = co2_variabledeclaration;
    }
    public co2_Expression getCo2_expression() {
        return co2_expression;
    }

    public void setCo2_expression(co2_Expression co2_expression) {
        this.co2_expression = co2_expression;
    }
    public co2_Process getCo2_process() {
        return co2_process;
    }

    public void setCo2_process(co2_Process co2_process) {
        this.co2_process = co2_process;
    }
    public co2_IntAction getCo2_intaction() {
        return co2_intaction;
    }

    public void setCo2_intaction(co2_IntAction co2_intaction) {
        this.co2_intaction = co2_intaction;
    }

}
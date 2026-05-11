





import java.util.List;
import java.util.ArrayList;

public class arduino_VariableRef extends Expression {






    private arduino_Variable arduino_variable;


    public arduino_VariableRef(
    ) {
        super(
        );
    }



    public arduino_Variable getArduino_variable() {
        return arduino_variable;
    }

    public void setArduino_variable(arduino_Variable arduino_variable) {
        this.arduino_variable = arduino_variable;
    }

}
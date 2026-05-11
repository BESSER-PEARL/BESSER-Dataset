





import java.util.List;
import java.util.ArrayList;

public class arduino_IntegerVariableRef extends IntegerExpression, VariableRef {






    private arduino_IntegerVariable arduino_integervariable;


    public arduino_IntegerVariableRef(
    ) {
        super(
        );
    }



    public arduino_IntegerVariable getArduino_integervariable() {
        return arduino_integervariable;
    }

    public void setArduino_integervariable(arduino_IntegerVariable arduino_integervariable) {
        this.arduino_integervariable = arduino_integervariable;
    }

}






import java.util.List;
import java.util.ArrayList;

public class arduino_Value extends Instruction, Parameter {

    private String value;





    private arduino_MathOperator arduino_mathoperator;




    private arduino_MathOperator arduino_mathoperator;




    private arduino_Set arduino_set;


    public arduino_Value(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public arduino_MathOperator getArduino_mathoperator() {
        return arduino_mathoperator;
    }

    public void setArduino_mathoperator(arduino_MathOperator arduino_mathoperator) {
        this.arduino_mathoperator = arduino_mathoperator;
    }
    public arduino_MathOperator getArduino_mathoperator() {
        return arduino_mathoperator;
    }

    public void setArduino_mathoperator(arduino_MathOperator arduino_mathoperator) {
        this.arduino_mathoperator = arduino_mathoperator;
    }
    public arduino_Set getArduino_set() {
        return arduino_set;
    }

    public void setArduino_set(arduino_Set arduino_set) {
        this.arduino_set = arduino_set;
    }

}
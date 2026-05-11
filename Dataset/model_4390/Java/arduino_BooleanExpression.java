





import java.util.List;
import java.util.ArrayList;

public class arduino_BooleanExpression extends Expression {






    private arduino_If arduino_if;




    private arduino_While arduino_while;


    public arduino_BooleanExpression(
    ) {
        super(
        );
    }



    public arduino_If getArduino_if() {
        return arduino_if;
    }

    public void setArduino_if(arduino_If arduino_if) {
        this.arduino_if = arduino_if;
    }
    public arduino_While getArduino_while() {
        return arduino_while;
    }

    public void setArduino_while(arduino_While arduino_while) {
        this.arduino_while = arduino_while;
    }

}
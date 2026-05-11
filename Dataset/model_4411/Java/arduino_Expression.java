





import java.util.List;
import java.util.ArrayList;

public class arduino_Expression  {






    private arduino_UnaryExpression arduino_unaryexpression;




    private arduino_While arduino_while;




    private arduino_BinaryExpression arduino_binaryexpression;




    private arduino_BinaryExpression arduino_binaryexpression;




    private arduino_Assignment arduino_assignment;




    private arduino_If arduino_if;


    public arduino_Expression(
    ) {
    }



    public arduino_UnaryExpression getArduino_unaryexpression() {
        return arduino_unaryexpression;
    }

    public void setArduino_unaryexpression(arduino_UnaryExpression arduino_unaryexpression) {
        this.arduino_unaryexpression = arduino_unaryexpression;
    }
    public arduino_While getArduino_while() {
        return arduino_while;
    }

    public void setArduino_while(arduino_While arduino_while) {
        this.arduino_while = arduino_while;
    }
    public arduino_BinaryExpression getArduino_binaryexpression() {
        return arduino_binaryexpression;
    }

    public void setArduino_binaryexpression(arduino_BinaryExpression arduino_binaryexpression) {
        this.arduino_binaryexpression = arduino_binaryexpression;
    }
    public arduino_BinaryExpression getArduino_binaryexpression() {
        return arduino_binaryexpression;
    }

    public void setArduino_binaryexpression(arduino_BinaryExpression arduino_binaryexpression) {
        this.arduino_binaryexpression = arduino_binaryexpression;
    }
    public arduino_Assignment getArduino_assignment() {
        return arduino_assignment;
    }

    public void setArduino_assignment(arduino_Assignment arduino_assignment) {
        this.arduino_assignment = arduino_assignment;
    }
    public arduino_If getArduino_if() {
        return arduino_if;
    }

    public void setArduino_if(arduino_If arduino_if) {
        this.arduino_if = arduino_if;
    }

}
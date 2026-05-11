





import java.util.List;
import java.util.ArrayList;

public class arduino_Variable extends NamedElement {






    private arduino_VariableDeclaration arduino_variabledeclaration;




    private arduino_VariableAssignment arduino_variableassignment;


    public arduino_Variable(
    ) {
        super(
        );
    }



    public arduino_VariableDeclaration getArduino_variabledeclaration() {
        return arduino_variabledeclaration;
    }

    public void setArduino_variabledeclaration(arduino_VariableDeclaration arduino_variabledeclaration) {
        this.arduino_variabledeclaration = arduino_variabledeclaration;
    }
    public arduino_VariableAssignment getArduino_variableassignment() {
        return arduino_variableassignment;
    }

    public void setArduino_variableassignment(arduino_VariableAssignment arduino_variableassignment) {
        this.arduino_variableassignment = arduino_variableassignment;
    }

}
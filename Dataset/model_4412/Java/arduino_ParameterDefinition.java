





import java.util.List;
import java.util.ArrayList;

public class arduino_ParameterDefinition  {

    private String type;
    private String name;





    private arduino_ParameterCall arduino_parametercall;




    private arduino_Function arduino_function;


    public arduino_ParameterDefinition(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public arduino_ParameterCall getArduino_parametercall() {
        return arduino_parametercall;
    }

    public void setArduino_parametercall(arduino_ParameterCall arduino_parametercall) {
        this.arduino_parametercall = arduino_parametercall;
    }
    public arduino_Function getArduino_function() {
        return arduino_function;
    }

    public void setArduino_function(arduino_Function arduino_function) {
        this.arduino_function = arduino_function;
    }

}






import java.util.List;
import java.util.ArrayList;

public class arduino_If extends Control {






    private arduino_Expression arduino_expression;




    private arduino_Block arduino_block;


    public arduino_If(
    ) {
        super(
        );
    }



    public arduino_Expression getArduino_expression() {
        return arduino_expression;
    }

    public void setArduino_expression(arduino_Expression arduino_expression) {
        this.arduino_expression = arduino_expression;
    }
    public arduino_Block getArduino_block() {
        return arduino_block;
    }

    public void setArduino_block(arduino_Block arduino_block) {
        this.arduino_block = arduino_block;
    }

}
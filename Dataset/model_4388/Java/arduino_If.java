





import java.util.List;
import java.util.ArrayList;

public class arduino_If extends Control {






    private arduino_BooleanExpression arduino_booleanexpression;




    private arduino_Block arduino_block;


    public arduino_If(
    ) {
        super(
        );
    }



    public arduino_BooleanExpression getArduino_booleanexpression() {
        return arduino_booleanexpression;
    }

    public void setArduino_booleanexpression(arduino_BooleanExpression arduino_booleanexpression) {
        this.arduino_booleanexpression = arduino_booleanexpression;
    }
    public arduino_Block getArduino_block() {
        return arduino_block;
    }

    public void setArduino_block(arduino_Block arduino_block) {
        this.arduino_block = arduino_block;
    }

}
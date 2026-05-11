





import java.util.List;
import java.util.ArrayList;

public class arduino_Sketch extends NamedElement {






    private arduino_Board arduino_board;




    private arduino_Block arduino_block;


    public arduino_Sketch(
    ) {
        super(
        );
    }



    public arduino_Board getArduino_board() {
        return arduino_board;
    }

    public void setArduino_board(arduino_Board arduino_board) {
        this.arduino_board = arduino_board;
    }
    public arduino_Block getArduino_block() {
        return arduino_block;
    }

    public void setArduino_block(arduino_Block arduino_block) {
        this.arduino_block = arduino_block;
    }

}
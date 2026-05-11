





import java.util.List;
import java.util.ArrayList;

public class arduino_Module extends NamedElement {

    private String level;





    private arduino_Board arduino_board;


    public arduino_Module(
        String level    ) {
        super(
        );
        this.level = level;
    }


    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }

    public arduino_Board getArduino_board() {
        return arduino_board;
    }

    public void setArduino_board(arduino_Board arduino_board) {
        this.arduino_board = arduino_board;
    }

}
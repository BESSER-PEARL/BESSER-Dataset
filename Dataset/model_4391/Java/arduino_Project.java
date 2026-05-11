





import java.util.List;
import java.util.ArrayList;

public class arduino_Project  {






    private List<arduino_Sketch> arduino_sketchs;




    private List<arduino_Board> arduino_boards;




    private arduino_Board arduino_board;




    private arduino_Sketch arduino_sketch;


    public arduino_Project(
    ) {
        this.arduino_sketchs = new ArrayList<>();
        this.arduino_boards = new ArrayList<>();
    }

    public arduino_Project(
        ArrayList<arduino_Sketch> arduino_sketchs,        ArrayList<arduino_Board> arduino_boards    ) {
        this.arduino_sketchs = arduino_sketchs;
        this.arduino_boards = arduino_boards;
    }


    public List<arduino_Sketch> getArduino_sketchs() {
        return arduino_sketchs;
    }

    public void addArduino_sketch(Arduino_sketch arduino_sketch) {
        this.arduino_sketchs.add(arduino_sketch);
    }
    public List<arduino_Board> getArduino_boards() {
        return arduino_boards;
    }

    public void addArduino_board(Arduino_board arduino_board) {
        this.arduino_boards.add(arduino_board);
    }
    public arduino_Board getArduino_board() {
        return arduino_board;
    }

    public void setArduino_board(arduino_Board arduino_board) {
        this.arduino_board = arduino_board;
    }
    public arduino_Sketch getArduino_sketch() {
        return arduino_sketch;
    }

    public void setArduino_sketch(arduino_Sketch arduino_sketch) {
        this.arduino_sketch = arduino_sketch;
    }

}
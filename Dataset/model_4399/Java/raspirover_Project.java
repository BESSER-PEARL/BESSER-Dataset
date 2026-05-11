





import java.util.List;
import java.util.ArrayList;

public class raspirover_Project  {






    private raspirover_Sketch raspirover_sketch;




    private List<raspirover_Board> raspirover_boards;




    private List<raspirover_Sketch> raspirover_sketchs;




    private raspirover_Board raspirover_board;


    public raspirover_Project(
    ) {
        this.raspirover_boards = new ArrayList<>();
        this.raspirover_sketchs = new ArrayList<>();
    }

    public raspirover_Project(
        ArrayList<raspirover_Board> raspirover_boards,        ArrayList<raspirover_Sketch> raspirover_sketchs    ) {
        this.raspirover_boards = raspirover_boards;
        this.raspirover_sketchs = raspirover_sketchs;
    }


    public raspirover_Sketch getRaspirover_sketch() {
        return raspirover_sketch;
    }

    public void setRaspirover_sketch(raspirover_Sketch raspirover_sketch) {
        this.raspirover_sketch = raspirover_sketch;
    }
    public List<raspirover_Board> getRaspirover_boards() {
        return raspirover_boards;
    }

    public void addRaspirover_board(Raspirover_board raspirover_board) {
        this.raspirover_boards.add(raspirover_board);
    }
    public List<raspirover_Sketch> getRaspirover_sketchs() {
        return raspirover_sketchs;
    }

    public void addRaspirover_sketch(Raspirover_sketch raspirover_sketch) {
        this.raspirover_sketchs.add(raspirover_sketch);
    }
    public raspirover_Board getRaspirover_board() {
        return raspirover_board;
    }

    public void setRaspirover_board(raspirover_Board raspirover_board) {
        this.raspirover_board = raspirover_board;
    }

}
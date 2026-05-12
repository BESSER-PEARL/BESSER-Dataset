





import java.util.List;
import java.util.ArrayList;

public class Board  {

    private String board;





    private Window window;




    private GraphicsGenerator graphicsgenerator;


    public Board(
        String board    ) {
        this.board = board;
    }


    public String getBoard() {
        return board;
    }

    public void setBoard(String board) {
        this.board = board;
    }

    public Window getWindow() {
        return window;
    }

    public void setWindow(Window window) {
        this.window = window;
    }
    public GraphicsGenerator getGraphicsgenerator() {
        return graphicsgenerator;
    }

    public void setGraphicsgenerator(GraphicsGenerator graphicsgenerator) {
        this.graphicsgenerator = graphicsgenerator;
    }

}
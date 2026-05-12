





import java.util.List;
import java.util.ArrayList;

public class GameEngine  {






    private Board board;




    private EventHandler eventhandler;


    public GameEngine(
    ) {
    }



    public Board getBoard() {
        return board;
    }

    public void setBoard(Board board) {
        this.board = board;
    }
    public EventHandler getEventhandler() {
        return eventhandler;
    }

    public void setEventhandler(EventHandler eventhandler) {
        this.eventhandler = eventhandler;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Player  {






    private Snake snake;




    private GameSession gamesession;


    public Player(
    ) {
    }



    public Snake getSnake() {
        return snake;
    }

    public void setSnake(Snake snake) {
        this.snake = snake;
    }
    public GameSession getGamesession() {
        return gamesession;
    }

    public void setGamesession(GameSession gamesession) {
        this.gamesession = gamesession;
    }

}
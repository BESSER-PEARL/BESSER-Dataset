





import java.util.List;
import java.util.ArrayList;

public class MineField  {

    private String grid;
    private int width;
    private int height;





    private Game game;


    public MineField(
        String grid,        int width,        int height    ) {
        this.grid = grid;
        this.width = width;
        this.height = height;
    }


    public String getGrid() {
        return grid;
    }

    public void setGrid(String grid) {
        this.grid = grid;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }

    public Game getGame() {
        return game;
    }

    public void setGame(Game game) {
        this.game = game;
    }

}
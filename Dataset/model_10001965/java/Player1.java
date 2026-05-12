





import java.util.List;
import java.util.ArrayList;

public class Player1  {

    private int pocket;
    private String name;





    private GameRole gamerole;


    public Player1(
        int pocket,        String name    ) {
        this.pocket = pocket;
        this.name = name;
    }


    public int getPocket() {
        return pocket;
    }

    public void setPocket(int pocket) {
        this.pocket = pocket;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public GameRole getGamerole() {
        return gamerole;
    }

    public void setGamerole(GameRole gamerole) {
        this.gamerole = gamerole;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Player  {

    private String name;
    private int pocket;



    public Player(
        String name,        int pocket    ) {
        this.name = name;
        this.pocket = pocket;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPocket() {
        return pocket;
    }

    public void setPocket(int pocket) {
        this.pocket = pocket;
    }


}
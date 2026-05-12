





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private String name;
    private None pieces;
    private None color;



    public Player(
        String name,        None pieces,        None color    ) {
        this.name = name;
        this.pieces = pieces;
        this.color = color;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getPieces() {
        return pieces;
    }

    public void setPieces(None pieces) {
        this.pieces = pieces;
    }
    public None getColor() {
        return color;
    }

    public void setColor(None color) {
        this.color = color;
    }


}
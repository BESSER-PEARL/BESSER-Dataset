





import java.util.List;
import java.util.ArrayList;

public class Model_Tile  {

    private String position;
    private int type;
    private int mod;
    private int id;



    public Model_Tile(
        String position,        int type,        int mod,        int id    ) {
        this.position = position;
        this.type = type;
        this.mod = mod;
        this.id = id;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public int getMod() {
        return mod;
    }

    public void setMod(int mod) {
        this.mod = mod;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}
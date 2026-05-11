





import java.util.List;
import java.util.ArrayList;

public class model_story_Panel  {

    private String id;
    private int y;
    private int x;



    public model_story_Panel(
        String id,        int y,        int x    ) {
        this.id = id;
        this.y = y;
        this.x = x;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }


}
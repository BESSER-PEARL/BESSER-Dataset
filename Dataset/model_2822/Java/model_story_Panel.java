





import java.util.List;
import java.util.ArrayList;

public class model_story_Panel  {

    private int x;
    private int y;
    private String id;



    public model_story_Panel(
        int x,        int y,        String id    ) {
        this.x = x;
        this.y = y;
        this.id = id;
    }


    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}
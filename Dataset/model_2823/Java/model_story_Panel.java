





import java.util.List;
import java.util.ArrayList;

public class model_story_Panel  {

    private int x;
    private String id;
    private int y;





    private story_model_Screen story_model_screen;




    private Storyboard storyboard;


    public model_story_Panel(
        int x,        String id,        int y    ) {
        this.x = x;
        this.id = id;
        this.y = y;
    }


    public int getX() {
        return x;
    }

    public void setX(int x) {
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

    public story_model_Screen getStory_model_screen() {
        return story_model_screen;
    }

    public void setStory_model_screen(story_model_Screen story_model_screen) {
        this.story_model_screen = story_model_screen;
    }
    public Storyboard getStoryboard() {
        return storyboard;
    }

    public void setStoryboard(Storyboard storyboard) {
        this.storyboard = storyboard;
    }

}
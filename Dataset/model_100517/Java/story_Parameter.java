





import java.util.List;
import java.util.ArrayList;

public class story_Parameter  {

    private String name;
    private String description;
    private String type;





    private story_Story story_story;


    public story_Parameter(
        String name,        String description,        String type    ) {
        this.name = name;
        this.description = description;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public story_Story getStory_story() {
        return story_story;
    }

    public void setStory_story(story_Story story_story) {
        this.story_story = story_story;
    }

}
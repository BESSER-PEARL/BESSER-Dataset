





import java.util.List;
import java.util.ArrayList;

public class story_Goal  {

    private String details;
    private String name;





    private story_Story story_story;




    private story_Persona story_persona;


    public story_Goal(
        String details,        String name    ) {
        this.details = details;
        this.name = name;
    }


    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public story_Story getStory_story() {
        return story_story;
    }

    public void setStory_story(story_Story story_story) {
        this.story_story = story_story;
    }
    public story_Persona getStory_persona() {
        return story_persona;
    }

    public void setStory_persona(story_Persona story_persona) {
        this.story_persona = story_persona;
    }

}
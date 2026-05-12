





import java.util.List;
import java.util.ArrayList;

public class story_ConditionalProtagonist  {

    private String condition;





    private List<story_Protagonist> story_protagonists;




    private story_Story story_story;


    public story_ConditionalProtagonist(
        String condition    ) {
        this.condition = condition;
        this.story_protagonists = new ArrayList<>();
    }

    public story_ConditionalProtagonist(
        String condition        ArrayList<story_Protagonist> story_protagonists    ) {
        this.condition = condition;
        this.story_protagonists = story_protagonists;
    }

    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }

    public List<story_Protagonist> getStory_protagonists() {
        return story_protagonists;
    }

    public void addStory_protagonist(Story_protagonist story_protagonist) {
        this.story_protagonists.add(story_protagonist);
    }
    public story_Story getStory_story() {
        return story_story;
    }

    public void setStory_story(story_Story story_story) {
        this.story_story = story_story;
    }

}
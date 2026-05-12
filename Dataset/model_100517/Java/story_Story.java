





import java.util.List;
import java.util.ArrayList;

public class story_Story extends StoryBase {

    private String goal;
    private String benefit;
    private boolean completed;





    private List<story_Protagonist> story_protagonists;




    private List<story_Theme> story_themes;




    private List<story_Scenario> story_scenarios;




    private story_Story story_story;


    public story_Story(
        String goal,        String benefit,        boolean completed    ) {
        super(
        );
        this.goal = goal;
        this.benefit = benefit;
        this.completed = completed;
        this.story_protagonists = new ArrayList<>();
        this.story_themes = new ArrayList<>();
        this.story_scenarios = new ArrayList<>();
    }

    public story_Story(
        String goal,        String benefit,        boolean completed        ArrayList<story_Protagonist> story_protagonists,        ArrayList<story_Theme> story_themes,        ArrayList<story_Scenario> story_scenarios    ) {
        this.goal = goal;
        this.benefit = benefit;
        this.completed = completed;
        this.story_protagonists = story_protagonists;
        this.story_themes = story_themes;
        this.story_scenarios = story_scenarios;
    }

    public String getGoal() {
        return goal;
    }

    public void setGoal(String goal) {
        this.goal = goal;
    }
    public String getBenefit() {
        return benefit;
    }

    public void setBenefit(String benefit) {
        this.benefit = benefit;
    }
    public boolean getCompleted() {
        return completed;
    }

    public void setCompleted(boolean completed) {
        this.completed = completed;
    }

    public List<story_Protagonist> getStory_protagonists() {
        return story_protagonists;
    }

    public void addStory_protagonist(Story_protagonist story_protagonist) {
        this.story_protagonists.add(story_protagonist);
    }
    public List<story_Theme> getStory_themes() {
        return story_themes;
    }

    public void addStory_theme(Story_theme story_theme) {
        this.story_themes.add(story_theme);
    }
    public List<story_Scenario> getStory_scenarios() {
        return story_scenarios;
    }

    public void addStory_scenario(Story_scenario story_scenario) {
        this.story_scenarios.add(story_scenario);
    }
    public story_Story getStory_story() {
        return story_story;
    }

    public void setStory_story(story_Story story_story) {
        this.story_story = story_story;
    }

}
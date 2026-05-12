





import java.util.List;
import java.util.ArrayList;

public class story_Actor extends Protagonist {






    private List<story_Role> story_roles;




    private story_Actor story_actor;




    private List<story_Actor> story_actors;


    public story_Actor(
    ) {
        super(
        );
        this.story_roles = new ArrayList<>();
        this.story_actors = new ArrayList<>();
    }

    public story_Actor(
        ArrayList<story_Role> story_roles,        ArrayList<story_Actor> story_actors    ) {
        this.story_roles = story_roles;
        this.story_actors = story_actors;
    }


    public List<story_Role> getStory_roles() {
        return story_roles;
    }

    public void addStory_role(Story_role story_role) {
        this.story_roles.add(story_role);
    }
    public story_Actor getStory_actor() {
        return story_actor;
    }

    public void setStory_actor(story_Actor story_actor) {
        this.story_actor = story_actor;
    }
    public List<story_Actor> getStory_actors() {
        return story_actors;
    }

    public void addStory_actor(Story_actor story_actor) {
        this.story_actors.add(story_actor);
    }

}
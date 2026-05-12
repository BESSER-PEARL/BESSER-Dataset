





import java.util.List;
import java.util.ArrayList;

public class story_Role extends Protagonist {






    private List<story_Role> story_roles;




    private story_Role story_role;


    public story_Role(
    ) {
        super(
        );
        this.story_roles = new ArrayList<>();
    }

    public story_Role(
        ArrayList<story_Role> story_roles    ) {
        this.story_roles = story_roles;
    }


    public List<story_Role> getStory_roles() {
        return story_roles;
    }

    public void addStory_role(Story_role story_role) {
        this.story_roles.add(story_role);
    }
    public story_Role getStory_role() {
        return story_role;
    }

    public void setStory_role(story_Role story_role) {
        this.story_role = story_role;
    }

}
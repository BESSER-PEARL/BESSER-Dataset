





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Actor extends Element {

    private String FTEs;
    private String actorGoal;
    private String actorTasks;





    private contentfwk_OrganizationUnit contentfwk_organizationunit;




    private List<contentfwk_Actor> contentfwk_actors;




    private contentfwk_OrganizationUnit contentfwk_organizationunit;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;


    public contentfwk_Actor(
        String FTEs,        String actorGoal,        String actorTasks    ) {
        super(
        );
        this.FTEs = FTEs;
        this.actorGoal = actorGoal;
        this.actorTasks = actorTasks;
        this.contentfwk_actors = new ArrayList<>();
    }

    public contentfwk_Actor(
        String FTEs,        String actorGoal,        String actorTasks        ArrayList<contentfwk_Actor> contentfwk_actors    ) {
        this.FTEs = FTEs;
        this.actorGoal = actorGoal;
        this.actorTasks = actorTasks;
        this.contentfwk_actors = contentfwk_actors;
    }

    public String getFtes() {
        return FTEs;
    }

    public void setFtes(String FTEs) {
        this.FTEs = FTEs;
    }
    public String getActorgoal() {
        return actorGoal;
    }

    public void setActorgoal(String actorGoal) {
        this.actorGoal = actorGoal;
    }
    public String getActortasks() {
        return actorTasks;
    }

    public void setActortasks(String actorTasks) {
        this.actorTasks = actorTasks;
    }

    public contentfwk_OrganizationUnit getContentfwk_organizationunit() {
        return contentfwk_organizationunit;
    }

    public void setContentfwk_organizationunit(contentfwk_OrganizationUnit contentfwk_organizationunit) {
        this.contentfwk_organizationunit = contentfwk_organizationunit;
    }
    public List<contentfwk_Actor> getContentfwk_actors() {
        return contentfwk_actors;
    }

    public void addContentfwk_actor(Contentfwk_actor contentfwk_actor) {
        this.contentfwk_actors.add(contentfwk_actor);
    }
    public contentfwk_OrganizationUnit getContentfwk_organizationunit() {
        return contentfwk_organizationunit;
    }

    public void setContentfwk_organizationunit(contentfwk_OrganizationUnit contentfwk_organizationunit) {
        this.contentfwk_organizationunit = contentfwk_organizationunit;
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }

}
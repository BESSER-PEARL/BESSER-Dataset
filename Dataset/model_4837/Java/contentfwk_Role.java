





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Role extends Element {

    private String estimatedFTEs;





    private contentfwk_Actor contentfwk_actor;




    private List<contentfwk_Actor> contentfwk_actors;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private contentfwk_Role contentfwk_role;


    public contentfwk_Role(
        String estimatedFTEs    ) {
        super(
        );
        this.estimatedFTEs = estimatedFTEs;
        this.contentfwk_actors = new ArrayList<>();
    }

    public contentfwk_Role(
        String estimatedFTEs        ArrayList<contentfwk_Actor> contentfwk_actors    ) {
        this.estimatedFTEs = estimatedFTEs;
        this.contentfwk_actors = contentfwk_actors;
    }

    public String getEstimatedftes() {
        return estimatedFTEs;
    }

    public void setEstimatedftes(String estimatedFTEs) {
        this.estimatedFTEs = estimatedFTEs;
    }

    public contentfwk_Actor getContentfwk_actor() {
        return contentfwk_actor;
    }

    public void setContentfwk_actor(contentfwk_Actor contentfwk_actor) {
        this.contentfwk_actor = contentfwk_actor;
    }
    public List<contentfwk_Actor> getContentfwk_actors() {
        return contentfwk_actors;
    }

    public void addContentfwk_actor(Contentfwk_actor contentfwk_actor) {
        this.contentfwk_actors.add(contentfwk_actor);
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public contentfwk_Role getContentfwk_role() {
        return contentfwk_role;
    }

    public void setContentfwk_role(contentfwk_Role contentfwk_role) {
        this.contentfwk_role = contentfwk_role;
    }

}
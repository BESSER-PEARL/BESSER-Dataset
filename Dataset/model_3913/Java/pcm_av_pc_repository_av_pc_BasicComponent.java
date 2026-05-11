





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_repository_av_pc_BasicComponent extends ImplementationComponentType {






    private List<PassiveResource> passiveresources;


    public pcm_av_pc_repository_av_pc_BasicComponent(
    ) {
        super(
        );
        this.passiveresources = new ArrayList<>();
    }

    public pcm_av_pc_repository_av_pc_BasicComponent(
        ArrayList<PassiveResource> passiveresources    ) {
        this.passiveresources = passiveresources;
    }


    public List<PassiveResource> getPassiveresources() {
        return passiveresources;
    }

    public void addPassiveresource(Passiveresource passiveresource) {
        this.passiveresources.add(passiveresource);
    }

}
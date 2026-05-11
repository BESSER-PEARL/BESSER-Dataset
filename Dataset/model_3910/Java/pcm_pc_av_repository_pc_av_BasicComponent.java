





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_av_repository_pc_av_BasicComponent extends ImplementationComponentType {






    private List<PassiveResource> passiveresources;


    public pcm_pc_av_repository_pc_av_BasicComponent(
    ) {
        super(
        );
        this.passiveresources = new ArrayList<>();
    }

    public pcm_pc_av_repository_pc_av_BasicComponent(
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
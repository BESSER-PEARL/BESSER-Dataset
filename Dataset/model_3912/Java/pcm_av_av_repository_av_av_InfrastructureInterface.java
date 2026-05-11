





import java.util.List;
import java.util.ArrayList;

public class pcm_av_av_repository_av_av_InfrastructureInterface extends Interface {






    private List<InfrastructureSignature> infrastructuresignatures;


    public pcm_av_av_repository_av_av_InfrastructureInterface(
    ) {
        super(
        );
        this.infrastructuresignatures = new ArrayList<>();
    }

    public pcm_av_av_repository_av_av_InfrastructureInterface(
        ArrayList<InfrastructureSignature> infrastructuresignatures    ) {
        this.infrastructuresignatures = infrastructuresignatures;
    }


    public List<InfrastructureSignature> getInfrastructuresignatures() {
        return infrastructuresignatures;
    }

    public void addInfrastructuresignature(Infrastructuresignature infrastructuresignature) {
        this.infrastructuresignatures.add(infrastructuresignature);
    }

}
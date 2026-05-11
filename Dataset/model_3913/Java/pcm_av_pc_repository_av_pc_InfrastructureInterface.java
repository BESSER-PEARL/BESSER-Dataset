





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_repository_av_pc_InfrastructureInterface extends Interface {






    private List<InfrastructureSignature> infrastructuresignatures;


    public pcm_av_pc_repository_av_pc_InfrastructureInterface(
    ) {
        super(
        );
        this.infrastructuresignatures = new ArrayList<>();
    }

    public pcm_av_pc_repository_av_pc_InfrastructureInterface(
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
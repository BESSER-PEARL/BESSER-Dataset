





import java.util.List;
import java.util.ArrayList;

public class p2_SimpleArtifactRepository extends IFileArtifactRepository, ArtifactRepository {






    private List<p2_MappingRule> p2_mappingrules;


    public p2_SimpleArtifactRepository(
    ) {
        super(
        );
        this.p2_mappingrules = new ArrayList<>();
    }

    public p2_SimpleArtifactRepository(
        ArrayList<p2_MappingRule> p2_mappingrules    ) {
        this.p2_mappingrules = p2_mappingrules;
    }


    public List<p2_MappingRule> getP2_mappingrules() {
        return p2_mappingrules;
    }

    public void addP2_mappingrule(P2_mappingrule p2_mappingrule) {
        this.p2_mappingrules.add(p2_mappingrule);
    }

}
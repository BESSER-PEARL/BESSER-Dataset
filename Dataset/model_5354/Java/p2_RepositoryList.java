





import java.util.List;
import java.util.ArrayList;

public class p2_RepositoryList extends ModelElement {

    private String name;





    private List<p2_Repository> p2_repositorys;


    public p2_RepositoryList(
        String name    ) {
        super(
        );
        this.name = name;
        this.p2_repositorys = new ArrayList<>();
    }

    public p2_RepositoryList(
        String name        ArrayList<p2_Repository> p2_repositorys    ) {
        this.name = name;
        this.p2_repositorys = p2_repositorys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<p2_Repository> getP2_repositorys() {
        return p2_repositorys;
    }

    public void addP2_repository(P2_repository p2_repository) {
        this.p2_repositorys.add(p2_repository);
    }

}
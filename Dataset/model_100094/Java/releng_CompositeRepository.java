





import java.util.List;
import java.util.ArrayList;

public class releng_CompositeRepository extends Repository {






    private List<releng_Repository> releng_repositorys;


    public releng_CompositeRepository(
    ) {
        super(
        );
        this.releng_repositorys = new ArrayList<>();
    }

    public releng_CompositeRepository(
        ArrayList<releng_Repository> releng_repositorys    ) {
        this.releng_repositorys = releng_repositorys;
    }


    public List<releng_Repository> getReleng_repositorys() {
        return releng_repositorys;
    }

    public void addReleng_repository(Releng_repository releng_repository) {
        this.releng_repositorys.add(releng_repository);
    }

}
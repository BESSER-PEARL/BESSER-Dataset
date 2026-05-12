





import java.util.List;
import java.util.ArrayList;

public class setup_RepositoryList  {

    private String name;





    private List<setup_P2Repository> setup_p2repositorys;


    public setup_RepositoryList(
        String name    ) {
        this.name = name;
        this.setup_p2repositorys = new ArrayList<>();
    }

    public setup_RepositoryList(
        String name        ArrayList<setup_P2Repository> setup_p2repositorys    ) {
        this.name = name;
        this.setup_p2repositorys = setup_p2repositorys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<setup_P2Repository> getSetup_p2repositorys() {
        return setup_p2repositorys;
    }

    public void addSetup_p2repository(Setup_p2repository setup_p2repository) {
        this.setup_p2repositorys.add(setup_p2repository);
    }

}
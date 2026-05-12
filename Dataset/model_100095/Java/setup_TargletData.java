





import java.util.List;
import java.util.ArrayList;

public class setup_TargletData  {

    private String activeRepositoryList;
    private boolean includeAllPlatforms;
    private boolean includeSources;
    private String name;





    private List<setup_AutomaticSourceLocator> setup_automaticsourcelocators;




    private List<setup_InstallableUnit> setup_installableunits;




    private List<setup_RepositoryList> setup_repositorylists;




    private List<setup_P2Repository> setup_p2repositorys;


    public setup_TargletData(
        String activeRepositoryList,        boolean includeAllPlatforms,        boolean includeSources,        String name    ) {
        this.activeRepositoryList = activeRepositoryList;
        this.includeAllPlatforms = includeAllPlatforms;
        this.includeSources = includeSources;
        this.name = name;
        this.setup_automaticsourcelocators = new ArrayList<>();
        this.setup_installableunits = new ArrayList<>();
        this.setup_repositorylists = new ArrayList<>();
        this.setup_p2repositorys = new ArrayList<>();
    }

    public setup_TargletData(
        String activeRepositoryList,        boolean includeAllPlatforms,        boolean includeSources,        String name        ArrayList<setup_AutomaticSourceLocator> setup_automaticsourcelocators,        ArrayList<setup_InstallableUnit> setup_installableunits,        ArrayList<setup_RepositoryList> setup_repositorylists,        ArrayList<setup_P2Repository> setup_p2repositorys    ) {
        this.activeRepositoryList = activeRepositoryList;
        this.includeAllPlatforms = includeAllPlatforms;
        this.includeSources = includeSources;
        this.name = name;
        this.setup_automaticsourcelocators = setup_automaticsourcelocators;
        this.setup_installableunits = setup_installableunits;
        this.setup_repositorylists = setup_repositorylists;
        this.setup_p2repositorys = setup_p2repositorys;
    }

    public String getActiverepositorylist() {
        return activeRepositoryList;
    }

    public void setActiverepositorylist(String activeRepositoryList) {
        this.activeRepositoryList = activeRepositoryList;
    }
    public boolean getIncludeallplatforms() {
        return includeAllPlatforms;
    }

    public void setIncludeallplatforms(boolean includeAllPlatforms) {
        this.includeAllPlatforms = includeAllPlatforms;
    }
    public boolean getIncludesources() {
        return includeSources;
    }

    public void setIncludesources(boolean includeSources) {
        this.includeSources = includeSources;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<setup_AutomaticSourceLocator> getSetup_automaticsourcelocators() {
        return setup_automaticsourcelocators;
    }

    public void addSetup_automaticsourcelocator(Setup_automaticsourcelocator setup_automaticsourcelocator) {
        this.setup_automaticsourcelocators.add(setup_automaticsourcelocator);
    }
    public List<setup_InstallableUnit> getSetup_installableunits() {
        return setup_installableunits;
    }

    public void addSetup_installableunit(Setup_installableunit setup_installableunit) {
        this.setup_installableunits.add(setup_installableunit);
    }
    public List<setup_RepositoryList> getSetup_repositorylists() {
        return setup_repositorylists;
    }

    public void addSetup_repositorylist(Setup_repositorylist setup_repositorylist) {
        this.setup_repositorylists.add(setup_repositorylist);
    }
    public List<setup_P2Repository> getSetup_p2repositorys() {
        return setup_p2repositorys;
    }

    public void addSetup_p2repository(Setup_p2repository setup_p2repository) {
        this.setup_p2repositorys.add(setup_p2repository);
    }

}
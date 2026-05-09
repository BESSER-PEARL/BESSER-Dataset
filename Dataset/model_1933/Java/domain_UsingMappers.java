





import java.util.List;
import java.util.ArrayList;

public class domain_UsingMappers  {






    private List<domain_ApplicationMapper> domain_applicationmappers;


    public domain_UsingMappers(
    ) {
        this.domain_applicationmappers = new ArrayList<>();
    }

    public domain_UsingMappers(
        ArrayList<domain_ApplicationMapper> domain_applicationmappers    ) {
        this.domain_applicationmappers = domain_applicationmappers;
    }


    public List<domain_ApplicationMapper> getDomain_applicationmappers() {
        return domain_applicationmappers;
    }

    public void addDomain_applicationmapper(Domain_applicationmapper domain_applicationmapper) {
        this.domain_applicationmappers.add(domain_applicationmapper);
    }

}
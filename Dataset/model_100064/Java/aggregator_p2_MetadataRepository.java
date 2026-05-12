





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_MetadataRepository extends IMetadataRepository {






    private List<Property> propertys;




    private List<RepositoryReference> repositoryreferences;


    public aggregator_p2_MetadataRepository(
    ) {
        super(
        );
        this.propertys = new ArrayList<>();
        this.repositoryreferences = new ArrayList<>();
    }

    public aggregator_p2_MetadataRepository(
        ArrayList<Property> propertys,        ArrayList<RepositoryReference> repositoryreferences    ) {
        this.propertys = propertys;
        this.repositoryreferences = repositoryreferences;
    }


    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }
    public List<RepositoryReference> getRepositoryreferences() {
        return repositoryreferences;
    }

    public void addRepositoryreference(Repositoryreference repositoryreference) {
        this.repositoryreferences.add(repositoryreference);
    }

}
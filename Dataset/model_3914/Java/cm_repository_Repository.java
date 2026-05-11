





import java.util.List;
import java.util.ArrayList;

public class cm_repository_Repository extends Entity {

    private String description;





    private List<RepositoryComponent> repositorycomponents;




    private List<Interface> interfaces;




    private List<DataType> datatypes;


    public cm_repository_Repository(
        String description    ) {
        super(
        );
        this.description = description;
        this.repositorycomponents = new ArrayList<>();
        this.interfaces = new ArrayList<>();
        this.datatypes = new ArrayList<>();
    }

    public cm_repository_Repository(
        String description        ArrayList<RepositoryComponent> repositorycomponents,        ArrayList<Interface> interfaces,        ArrayList<DataType> datatypes    ) {
        this.description = description;
        this.repositorycomponents = repositorycomponents;
        this.interfaces = interfaces;
        this.datatypes = datatypes;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<RepositoryComponent> getRepositorycomponents() {
        return repositorycomponents;
    }

    public void addRepositorycomponent(Repositorycomponent repositorycomponent) {
        this.repositorycomponents.add(repositorycomponent);
    }
    public List<Interface> getInterfaces() {
        return interfaces;
    }

    public void addInterface(Interface interface) {
        this.interfaces.add(interface);
    }
    public List<DataType> getDatatypes() {
        return datatypes;
    }

    public void addDatatype(Datatype datatype) {
        this.datatypes.add(datatype);
    }

}






import java.util.List;
import java.util.ArrayList;

public class library_ReferenceNetwork extends Base {

    private String name;
    private String description;





    private List<library_ReferenceNetwork> library_referencenetworks;


    public library_ReferenceNetwork(
        String name,        String description    ) {
        super(
        );
        this.name = name;
        this.description = description;
        this.library_referencenetworks = new ArrayList<>();
    }

    public library_ReferenceNetwork(
        String name,        String description        ArrayList<library_ReferenceNetwork> library_referencenetworks    ) {
        this.name = name;
        this.description = description;
        this.library_referencenetworks = library_referencenetworks;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<library_ReferenceNetwork> getLibrary_referencenetworks() {
        return library_referencenetworks;
    }

    public void addLibrary_referencenetwork(Library_referencenetwork library_referencenetwork) {
        this.library_referencenetworks.add(library_referencenetwork);
    }

}
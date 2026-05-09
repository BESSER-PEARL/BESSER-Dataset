





import java.util.List;
import java.util.ArrayList;

public class emof_Package extends NamedElement {

    private String uri;





    private emof_Type emof_type;




    private List<emof_Package> emof_packages;




    private List<emof_Type> emof_types;


    public emof_Package(
        String uri    ) {
        super(
        );
        this.uri = uri;
        this.emof_packages = new ArrayList<>();
        this.emof_types = new ArrayList<>();
    }

    public emof_Package(
        String uri        ArrayList<emof_Package> emof_packages,        ArrayList<emof_Type> emof_types    ) {
        this.uri = uri;
        this.emof_packages = emof_packages;
        this.emof_types = emof_types;
    }

    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public emof_Type getEmof_type() {
        return emof_type;
    }

    public void setEmof_type(emof_Type emof_type) {
        this.emof_type = emof_type;
    }
    public List<emof_Package> getEmof_packages() {
        return emof_packages;
    }

    public void addEmof_package(Emof_package emof_package) {
        this.emof_packages.add(emof_package);
    }
    public List<emof_Type> getEmof_types() {
        return emof_types;
    }

    public void addEmof_type(Emof_type emof_type) {
        this.emof_types.add(emof_type);
    }

}
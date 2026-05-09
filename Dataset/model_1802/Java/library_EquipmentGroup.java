





import java.util.List;
import java.util.ArrayList;

public class library_EquipmentGroup extends Base {

    private String name;
    private String description;
    private String count;





    private List<library_NetXResource> library_netxresources;




    private List<library_NetXResource> library_netxresources;




    private List<library_Expression> library_expressions;


    public library_EquipmentGroup(
        String name,        String description,        String count    ) {
        super(
        );
        this.name = name;
        this.description = description;
        this.count = count;
        this.library_netxresources = new ArrayList<>();
        this.library_netxresources = new ArrayList<>();
        this.library_expressions = new ArrayList<>();
    }

    public library_EquipmentGroup(
        String name,        String description,        String count        ArrayList<library_NetXResource> library_netxresources,        ArrayList<library_NetXResource> library_netxresources,        ArrayList<library_Expression> library_expressions    ) {
        this.name = name;
        this.description = description;
        this.count = count;
        this.library_netxresources = library_netxresources;
        this.library_netxresources = library_netxresources;
        this.library_expressions = library_expressions;
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
    public String getCount() {
        return count;
    }

    public void setCount(String count) {
        this.count = count;
    }

    public List<library_NetXResource> getLibrary_netxresources() {
        return library_netxresources;
    }

    public void addLibrary_netxresource(Library_netxresource library_netxresource) {
        this.library_netxresources.add(library_netxresource);
    }
    public List<library_NetXResource> getLibrary_netxresources() {
        return library_netxresources;
    }

    public void addLibrary_netxresource(Library_netxresource library_netxresource) {
        this.library_netxresources.add(library_netxresource);
    }
    public List<library_Expression> getLibrary_expressions() {
        return library_expressions;
    }

    public void addLibrary_expression(Library_expression library_expression) {
        this.library_expressions.add(library_expression);
    }

}
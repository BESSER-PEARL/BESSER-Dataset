





import java.util.List;
import java.util.ArrayList;

public class library_NodeType extends Base {

    private String name;
    private String leafNode;





    private List<library_Function> library_functions;




    private List<library_Equipment> library_equipments;


    public library_NodeType(
        String name,        String leafNode    ) {
        super(
        );
        this.name = name;
        this.leafNode = leafNode;
        this.library_functions = new ArrayList<>();
        this.library_equipments = new ArrayList<>();
    }

    public library_NodeType(
        String name,        String leafNode        ArrayList<library_Function> library_functions,        ArrayList<library_Equipment> library_equipments    ) {
        this.name = name;
        this.leafNode = leafNode;
        this.library_functions = library_functions;
        this.library_equipments = library_equipments;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLeafnode() {
        return leafNode;
    }

    public void setLeafnode(String leafNode) {
        this.leafNode = leafNode;
    }

    public List<library_Function> getLibrary_functions() {
        return library_functions;
    }

    public void addLibrary_function(Library_function library_function) {
        this.library_functions.add(library_function);
    }
    public List<library_Equipment> getLibrary_equipments() {
        return library_equipments;
    }

    public void addLibrary_equipment(Library_equipment library_equipment) {
        this.library_equipments.add(library_equipment);
    }

}
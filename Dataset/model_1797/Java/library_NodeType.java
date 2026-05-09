





import java.util.List;
import java.util.ArrayList;

public class library_NodeType  {

    private String leafNode;





    private List<library_Equipment> library_equipments;




    private List<library_Function> library_functions;




    private library_Library library_library;


    public library_NodeType(
        String leafNode    ) {
        this.leafNode = leafNode;
        this.library_equipments = new ArrayList<>();
        this.library_functions = new ArrayList<>();
    }

    public library_NodeType(
        String leafNode        ArrayList<library_Equipment> library_equipments,        ArrayList<library_Function> library_functions    ) {
        this.leafNode = leafNode;
        this.library_equipments = library_equipments;
        this.library_functions = library_functions;
    }

    public String getLeafnode() {
        return leafNode;
    }

    public void setLeafnode(String leafNode) {
        this.leafNode = leafNode;
    }

    public List<library_Equipment> getLibrary_equipments() {
        return library_equipments;
    }

    public void addLibrary_equipment(Library_equipment library_equipment) {
        this.library_equipments.add(library_equipment);
    }
    public List<library_Function> getLibrary_functions() {
        return library_functions;
    }

    public void addLibrary_function(Library_function library_function) {
        this.library_functions.add(library_function);
    }
    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }

}
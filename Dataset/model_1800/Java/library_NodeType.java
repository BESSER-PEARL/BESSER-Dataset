





import java.util.List;
import java.util.ArrayList;

public class library_NodeType  {






    private List<library_Function> library_functions;




    private library_Library library_library;




    private List<library_Equipment> library_equipments;


    public library_NodeType(
    ) {
        this.library_functions = new ArrayList<>();
        this.library_equipments = new ArrayList<>();
    }

    public library_NodeType(
        ArrayList<library_Function> library_functions,        ArrayList<library_Equipment> library_equipments    ) {
        this.library_functions = library_functions;
        this.library_equipments = library_equipments;
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
    public List<library_Equipment> getLibrary_equipments() {
        return library_equipments;
    }

    public void addLibrary_equipment(Library_equipment library_equipment) {
        this.library_equipments.add(library_equipment);
    }

}
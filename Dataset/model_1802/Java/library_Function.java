





import java.util.List;
import java.util.ArrayList;

public class library_Function extends Component {






    private library_ProductInfo library_productinfo;




    private List<library_Function> library_functions;




    private library_NodeType library_nodetype;




    private List<library_Function> library_functions;


    public library_Function(
    ) {
        super(
        );
        this.library_functions = new ArrayList<>();
        this.library_functions = new ArrayList<>();
    }

    public library_Function(
        ArrayList<library_Function> library_functions,        ArrayList<library_Function> library_functions    ) {
        this.library_functions = library_functions;
        this.library_functions = library_functions;
    }


    public library_ProductInfo getLibrary_productinfo() {
        return library_productinfo;
    }

    public void setLibrary_productinfo(library_ProductInfo library_productinfo) {
        this.library_productinfo = library_productinfo;
    }
    public List<library_Function> getLibrary_functions() {
        return library_functions;
    }

    public void addLibrary_function(Library_function library_function) {
        this.library_functions.add(library_function);
    }
    public library_NodeType getLibrary_nodetype() {
        return library_nodetype;
    }

    public void setLibrary_nodetype(library_NodeType library_nodetype) {
        this.library_nodetype = library_nodetype;
    }
    public List<library_Function> getLibrary_functions() {
        return library_functions;
    }

    public void addLibrary_function(Library_function library_function) {
        this.library_functions.add(library_function);
    }

}
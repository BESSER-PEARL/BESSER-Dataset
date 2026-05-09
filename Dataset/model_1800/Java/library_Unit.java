





import java.util.List;
import java.util.ArrayList;

public class library_Unit  {

    private String description;
    private String name;
    private String code;





    private library_NetXResource library_netxresource;




    private library_MultiImage library_multiimage;




    private library_Library library_library;


    public library_Unit(
        String description,        String name,        String code    ) {
        this.description = description;
        this.name = name;
        this.code = code;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public library_NetXResource getLibrary_netxresource() {
        return library_netxresource;
    }

    public void setLibrary_netxresource(library_NetXResource library_netxresource) {
        this.library_netxresource = library_netxresource;
    }
    public library_MultiImage getLibrary_multiimage() {
        return library_multiimage;
    }

    public void setLibrary_multiimage(library_MultiImage library_multiimage) {
        this.library_multiimage = library_multiimage;
    }
    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }

}






import java.util.List;
import java.util.ArrayList;

public class library_Unit extends Base {

    private String code;
    private String description;
    private String name;





    private library_Library library_library;




    private library_BaseResource library_baseresource;




    private library_MultiImage library_multiimage;


    public library_Unit(
        String code,        String description,        String name    ) {
        super(
        );
        this.code = code;
        this.description = description;
        this.name = name;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
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

    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }
    public library_BaseResource getLibrary_baseresource() {
        return library_baseresource;
    }

    public void setLibrary_baseresource(library_BaseResource library_baseresource) {
        this.library_baseresource = library_baseresource;
    }
    public library_MultiImage getLibrary_multiimage() {
        return library_multiimage;
    }

    public void setLibrary_multiimage(library_MultiImage library_multiimage) {
        this.library_multiimage = library_multiimage;
    }

}






import java.util.List;
import java.util.ArrayList;

public class library_Unit extends Base {

    private String code;
    private String name;
    private String description;





    private library_BaseResource library_baseresource;


    public library_Unit(
        String code,        String name,        String description    ) {
        super(
        );
        this.code = code;
        this.name = name;
        this.description = description;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
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

    public library_BaseResource getLibrary_baseresource() {
        return library_baseresource;
    }

    public void setLibrary_baseresource(library_BaseResource library_baseresource) {
        this.library_baseresource = library_baseresource;
    }

}
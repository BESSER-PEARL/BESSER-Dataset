





import java.util.List;
import java.util.ArrayList;

public class library_Unit extends Base {

    private String name;
    private String code;
    private String description;





    private library_BaseResource library_baseresource;


    public library_Unit(
        String name,        String code,        String description    ) {
        super(
        );
        this.name = name;
        this.code = code;
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
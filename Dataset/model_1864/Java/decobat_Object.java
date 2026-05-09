





import java.util.List;
import java.util.ArrayList;

public class decobat_Object  {

    private String shortDescription;
    private String description;
    private String name;
    private String code;





    private List<decobat_Library> decobat_librarys;


    public decobat_Object(
        String shortDescription,        String description,        String name,        String code    ) {
        this.shortDescription = shortDescription;
        this.description = description;
        this.name = name;
        this.code = code;
        this.decobat_librarys = new ArrayList<>();
    }

    public decobat_Object(
        String shortDescription,        String description,        String name,        String code        ArrayList<decobat_Library> decobat_librarys    ) {
        this.shortDescription = shortDescription;
        this.description = description;
        this.name = name;
        this.code = code;
        this.decobat_librarys = decobat_librarys;
    }

    public String getShortdescription() {
        return shortDescription;
    }

    public void setShortdescription(String shortDescription) {
        this.shortDescription = shortDescription;
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

    public List<decobat_Library> getDecobat_librarys() {
        return decobat_librarys;
    }

    public void addDecobat_library(Decobat_library decobat_library) {
        this.decobat_librarys.add(decobat_library);
    }

}
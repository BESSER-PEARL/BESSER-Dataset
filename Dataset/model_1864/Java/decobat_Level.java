





import java.util.List;
import java.util.ArrayList;

public class decobat_Level  {

    private String name;
    private String code;
    private String description;
    private String shortDescription;





    private List<decobat_Library> decobat_librarys;




    private decobat_Plan decobat_plan;


    public decobat_Level(
        String name,        String code,        String description,        String shortDescription    ) {
        this.name = name;
        this.code = code;
        this.description = description;
        this.shortDescription = shortDescription;
        this.decobat_librarys = new ArrayList<>();
    }

    public decobat_Level(
        String name,        String code,        String description,        String shortDescription        ArrayList<decobat_Library> decobat_librarys    ) {
        this.name = name;
        this.code = code;
        this.description = description;
        this.shortDescription = shortDescription;
        this.decobat_librarys = decobat_librarys;
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
    public String getShortdescription() {
        return shortDescription;
    }

    public void setShortdescription(String shortDescription) {
        this.shortDescription = shortDescription;
    }

    public List<decobat_Library> getDecobat_librarys() {
        return decobat_librarys;
    }

    public void addDecobat_library(Decobat_library decobat_library) {
        this.decobat_librarys.add(decobat_library);
    }
    public decobat_Plan getDecobat_plan() {
        return decobat_plan;
    }

    public void setDecobat_plan(decobat_Plan decobat_plan) {
        this.decobat_plan = decobat_plan;
    }

}
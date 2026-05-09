





import java.util.List;
import java.util.ArrayList;

public class decobat_Plan  {

    private String description;
    private String name;
    private String code;
    private String shortDescription;





    private decobat_Project decobat_project;


    public decobat_Plan(
        String description,        String name,        String code,        String shortDescription    ) {
        this.description = description;
        this.name = name;
        this.code = code;
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
    public String getShortdescription() {
        return shortDescription;
    }

    public void setShortdescription(String shortDescription) {
        this.shortDescription = shortDescription;
    }

    public decobat_Project getDecobat_project() {
        return decobat_project;
    }

    public void setDecobat_project(decobat_Project decobat_project) {
        this.decobat_project = decobat_project;
    }

}
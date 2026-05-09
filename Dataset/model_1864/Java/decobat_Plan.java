





import java.util.List;
import java.util.ArrayList;

public class decobat_Plan  {

    private String code;
    private String shortDescription;
    private String name;
    private String description;





    private decobat_Project decobat_project;


    public decobat_Plan(
        String code,        String shortDescription,        String name,        String description    ) {
        this.code = code;
        this.shortDescription = shortDescription;
        this.name = name;
        this.description = description;
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

    public decobat_Project getDecobat_project() {
        return decobat_project;
    }

    public void setDecobat_project(decobat_Project decobat_project) {
        this.decobat_project = decobat_project;
    }

}
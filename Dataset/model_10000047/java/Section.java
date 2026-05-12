





import java.util.List;
import java.util.ArrayList;

public class Section  {

    private String section_id;
    private String description;
    private String name;



    public Section(
        String section_id,        String description,        String name    ) {
        this.section_id = section_id;
        this.description = description;
        this.name = name;
    }


    public String getSection_id() {
        return section_id;
    }

    public void setSection_id(String section_id) {
        this.section_id = section_id;
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


}
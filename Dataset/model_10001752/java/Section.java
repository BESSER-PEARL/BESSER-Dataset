





import java.util.List;
import java.util.ArrayList;

public class Section  {

    private String description;
    private String section_id;
    private String name;



    public Section(
        String description,        String section_id,        String name    ) {
        this.description = description;
        this.section_id = section_id;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getSection_id() {
        return section_id;
    }

    public void setSection_id(String section_id) {
        this.section_id = section_id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
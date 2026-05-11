





import java.util.List;
import java.util.ArrayList;

public class mtm_di_Diagram  {

    private String resolution;
    private String name;
    private String documentation;
    private String id;



    public mtm_di_Diagram(
        String resolution,        String name,        String documentation,        String id    ) {
        this.resolution = resolution;
        this.name = name;
        this.documentation = documentation;
        this.id = id;
    }


    public String getResolution() {
        return resolution;
    }

    public void setResolution(String resolution) {
        this.resolution = resolution;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}
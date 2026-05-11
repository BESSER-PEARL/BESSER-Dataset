





import java.util.List;
import java.util.ArrayList;

public class di_Diagram  {

    private String documentation;
    private String name;
    private String resolution;
    private String id;



    public di_Diagram(
        String documentation,        String name,        String resolution,        String id    ) {
        this.documentation = documentation;
        this.name = name;
        this.resolution = resolution;
        this.id = id;
    }


    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getResolution() {
        return resolution;
    }

    public void setResolution(String resolution) {
        this.resolution = resolution;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}
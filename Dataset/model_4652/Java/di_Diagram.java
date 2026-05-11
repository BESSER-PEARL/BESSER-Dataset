





import java.util.List;
import java.util.ArrayList;

public class di_Diagram extends Shape {

    private String resolution;
    private String documentation;
    private String name;



    public di_Diagram(
        String resolution,        String documentation,        String name    ) {
        super(
        );
        this.resolution = resolution;
        this.documentation = documentation;
        this.name = name;
    }


    public String getResolution() {
        return resolution;
    }

    public void setResolution(String resolution) {
        this.resolution = resolution;
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


}






import java.util.List;
import java.util.ArrayList;

public class swrtj_Element  {

    private String construct;
    private String name;





    private swrtj_File swrtj_file;


    public swrtj_Element(
        String construct,        String name    ) {
        this.construct = construct;
        this.name = name;
    }


    public String getConstruct() {
        return construct;
    }

    public void setConstruct(String construct) {
        this.construct = construct;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public swrtj_File getSwrtj_file() {
        return swrtj_file;
    }

    public void setSwrtj_file(swrtj_File swrtj_file) {
        this.swrtj_file = swrtj_file;
    }

}
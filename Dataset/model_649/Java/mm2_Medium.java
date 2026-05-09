





import java.util.List;
import java.util.ArrayList;

public class mm2_Medium  {

    private String name;
    private String type;





    private mm2_Library mm2_library;


    public mm2_Medium(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public mm2_Library getMm2_library() {
        return mm2_library;
    }

    public void setMm2_library(mm2_Library mm2_library) {
        this.mm2_library = mm2_library;
    }

}
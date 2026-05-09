





import java.util.List;
import java.util.ArrayList;

public class mm3_Member  {

    private String name;





    private mm3_Library mm3_library;


    public mm3_Member(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mm3_Library getMm3_library() {
        return mm3_library;
    }

    public void setMm3_library(mm3_Library mm3_library) {
        this.mm3_library = mm3_library;
    }

}
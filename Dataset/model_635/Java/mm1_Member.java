





import java.util.List;
import java.util.ArrayList;

public class mm1_Member  {

    private String name;





    private mm1_Library mm1_library;


    public mm1_Member(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mm1_Library getMm1_library() {
        return mm1_library;
    }

    public void setMm1_library(mm1_Library mm1_library) {
        this.mm1_library = mm1_library;
    }

}
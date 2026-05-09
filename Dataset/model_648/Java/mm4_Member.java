





import java.util.List;
import java.util.ArrayList;

public class mm4_Member  {

    private String name;





    private mm4_Library mm4_library;


    public mm4_Member(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mm4_Library getMm4_library() {
        return mm4_library;
    }

    public void setMm4_library(mm4_Library mm4_library) {
        this.mm4_library = mm4_library;
    }

}
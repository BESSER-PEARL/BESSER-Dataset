





import java.util.List;
import java.util.ArrayList;

public class mm2_Book  {

    private String name;





    private mm2_Library mm2_library;


    public mm2_Book(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mm2_Library getMm2_library() {
        return mm2_library;
    }

    public void setMm2_library(mm2_Library mm2_library) {
        this.mm2_library = mm2_library;
    }

}
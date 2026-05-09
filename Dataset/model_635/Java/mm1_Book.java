





import java.util.List;
import java.util.ArrayList;

public class mm1_Book  {

    private String name;





    private mm1_Member mm1_member;




    private mm1_Library mm1_library;


    public mm1_Book(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mm1_Member getMm1_member() {
        return mm1_member;
    }

    public void setMm1_member(mm1_Member mm1_member) {
        this.mm1_member = mm1_member;
    }
    public mm1_Library getMm1_library() {
        return mm1_library;
    }

    public void setMm1_library(mm1_Library mm1_library) {
        this.mm1_library = mm1_library;
    }

}
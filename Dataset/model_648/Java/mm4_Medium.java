





import java.util.List;
import java.util.ArrayList;

public class mm4_Medium  {

    private String type;
    private String name;





    private mm4_Member mm4_member;




    private mm4_Library mm4_library;


    public mm4_Medium(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mm4_Member getMm4_member() {
        return mm4_member;
    }

    public void setMm4_member(mm4_Member mm4_member) {
        this.mm4_member = mm4_member;
    }
    public mm4_Library getMm4_library() {
        return mm4_library;
    }

    public void setMm4_library(mm4_Library mm4_library) {
        this.mm4_library = mm4_library;
    }

}
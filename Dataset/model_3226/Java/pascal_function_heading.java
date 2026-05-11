





import java.util.List;
import java.util.ArrayList;

public class pascal_function_heading  {

    private String id2;
    private String id1;





    private pascal_formal_parameter_list pascal_formal_parameter_list;


    public pascal_function_heading(
        String id2,        String id1    ) {
        this.id2 = id2;
        this.id1 = id1;
    }


    public String getId2() {
        return id2;
    }

    public void setId2(String id2) {
        this.id2 = id2;
    }
    public String getId1() {
        return id1;
    }

    public void setId1(String id1) {
        this.id1 = id1;
    }

    public pascal_formal_parameter_list getPascal_formal_parameter_list() {
        return pascal_formal_parameter_list;
    }

    public void setPascal_formal_parameter_list(pascal_formal_parameter_list pascal_formal_parameter_list) {
        this.pascal_formal_parameter_list = pascal_formal_parameter_list;
    }

}
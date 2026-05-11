





import java.util.List;
import java.util.ArrayList;

public class pascal_procedure_heading  {

    private String name;





    private pascal_formal_parameter_list pascal_formal_parameter_list;


    public pascal_procedure_heading(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pascal_formal_parameter_list getPascal_formal_parameter_list() {
        return pascal_formal_parameter_list;
    }

    public void setPascal_formal_parameter_list(pascal_formal_parameter_list pascal_formal_parameter_list) {
        this.pascal_formal_parameter_list = pascal_formal_parameter_list;
    }

}
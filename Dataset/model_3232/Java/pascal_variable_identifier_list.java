





import java.util.List;
import java.util.ArrayList;

public class pascal_variable_identifier_list  {

    private String names;





    private pascal_variable_section pascal_variable_section;


    public pascal_variable_identifier_list(
        String names    ) {
        this.names = names;
    }


    public String getNames() {
        return names;
    }

    public void setNames(String names) {
        this.names = names;
    }

    public pascal_variable_section getPascal_variable_section() {
        return pascal_variable_section;
    }

    public void setPascal_variable_section(pascal_variable_section pascal_variable_section) {
        this.pascal_variable_section = pascal_variable_section;
    }

}
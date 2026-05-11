





import java.util.List;
import java.util.ArrayList;

public class pascal_identifier_list  {

    private String names;





    private pascal_program_heading_block pascal_program_heading_block;


    public pascal_identifier_list(
        String names    ) {
        this.names = names;
    }


    public String getNames() {
        return names;
    }

    public void setNames(String names) {
        this.names = names;
    }

    public pascal_program_heading_block getPascal_program_heading_block() {
        return pascal_program_heading_block;
    }

    public void setPascal_program_heading_block(pascal_program_heading_block pascal_program_heading_block) {
        this.pascal_program_heading_block = pascal_program_heading_block;
    }

}






import java.util.List;
import java.util.ArrayList;

public class pascal_identifier_list  {

    private String ids;





    private pascal_program_heading pascal_program_heading;


    public pascal_identifier_list(
        String ids    ) {
        this.ids = ids;
    }


    public String getIds() {
        return ids;
    }

    public void setIds(String ids) {
        this.ids = ids;
    }

    public pascal_program_heading getPascal_program_heading() {
        return pascal_program_heading;
    }

    public void setPascal_program_heading(pascal_program_heading pascal_program_heading) {
        this.pascal_program_heading = pascal_program_heading;
    }

}
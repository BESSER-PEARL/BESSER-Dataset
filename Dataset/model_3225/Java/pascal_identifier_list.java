





import java.util.List;
import java.util.ArrayList;

public class pascal_identifier_list  {

    private String identifier;





    private pascal_program_heading pascal_program_heading;


    public pascal_identifier_list(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public pascal_program_heading getPascal_program_heading() {
        return pascal_program_heading;
    }

    public void setPascal_program_heading(pascal_program_heading pascal_program_heading) {
        this.pascal_program_heading = pascal_program_heading;
    }

}
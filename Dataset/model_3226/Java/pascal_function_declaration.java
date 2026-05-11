





import java.util.List;
import java.util.ArrayList;

public class pascal_function_declaration  {

    private String name;





    private pascal_type pascal_type;




    private pascal_block pascal_block;


    public pascal_function_declaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pascal_type getPascal_type() {
        return pascal_type;
    }

    public void setPascal_type(pascal_type pascal_type) {
        this.pascal_type = pascal_type;
    }
    public pascal_block getPascal_block() {
        return pascal_block;
    }

    public void setPascal_block(pascal_block pascal_block) {
        this.pascal_block = pascal_block;
    }

}
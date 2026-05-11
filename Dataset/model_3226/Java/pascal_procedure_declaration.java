





import java.util.List;
import java.util.ArrayList;

public class pascal_procedure_declaration  {

    private String name;





    private pascal_block pascal_block;


    public pascal_procedure_declaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pascal_block getPascal_block() {
        return pascal_block;
    }

    public void setPascal_block(pascal_block pascal_block) {
        this.pascal_block = pascal_block;
    }

}
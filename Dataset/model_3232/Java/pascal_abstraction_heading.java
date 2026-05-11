





import java.util.List;
import java.util.ArrayList;

public class pascal_abstraction_heading  {

    private String returnType;
    private String name;





    private pascal_abstraction_declaration pascal_abstraction_declaration;


    public pascal_abstraction_heading(
        String returnType,        String name    ) {
        this.returnType = returnType;
        this.name = name;
    }


    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pascal_abstraction_declaration getPascal_abstraction_declaration() {
        return pascal_abstraction_declaration;
    }

    public void setPascal_abstraction_declaration(pascal_abstraction_declaration pascal_abstraction_declaration) {
        this.pascal_abstraction_declaration = pascal_abstraction_declaration;
    }

}
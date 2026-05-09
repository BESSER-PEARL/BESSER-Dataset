





import java.util.List;
import java.util.ArrayList;

public class drn_Element  {

    private String name;





    private drn_TypeGeneric drn_typegeneric;




    private drn_Definition drn_definition;


    public drn_Element(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public drn_TypeGeneric getDrn_typegeneric() {
        return drn_typegeneric;
    }

    public void setDrn_typegeneric(drn_TypeGeneric drn_typegeneric) {
        this.drn_typegeneric = drn_typegeneric;
    }
    public drn_Definition getDrn_definition() {
        return drn_definition;
    }

    public void setDrn_definition(drn_Definition drn_definition) {
        this.drn_definition = drn_definition;
    }

}
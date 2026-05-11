





import java.util.List;
import java.util.ArrayList;

public class relational_Table  {

    private String name;





    private relational_Schema relational_schema;




    private relational_ForeignKey relational_foreignkey;


    public relational_Table(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public relational_Schema getRelational_schema() {
        return relational_schema;
    }

    public void setRelational_schema(relational_Schema relational_schema) {
        this.relational_schema = relational_schema;
    }
    public relational_ForeignKey getRelational_foreignkey() {
        return relational_foreignkey;
    }

    public void setRelational_foreignkey(relational_ForeignKey relational_foreignkey) {
        this.relational_foreignkey = relational_foreignkey;
    }

}
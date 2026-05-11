





import java.util.List;
import java.util.ArrayList;

public class database_Procedure extends RefProcedure {

    private String name;





    private database_RefType database_reftype;


    public database_Procedure(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public database_RefType getDatabase_reftype() {
        return database_reftype;
    }

    public void setDatabase_reftype(database_RefType database_reftype) {
        this.database_reftype = database_reftype;
    }

}
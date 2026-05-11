





import java.util.List;
import java.util.ArrayList;

public class database_Parameter extends RefParameter {

    private String name;





    private database_RefType database_reftype;


    public database_Parameter(
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
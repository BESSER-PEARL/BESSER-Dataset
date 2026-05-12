





import java.util.List;
import java.util.ArrayList;

public class dbca_DataParameter extends Parameter {

    private String type;





    private dbca_Function dbca_function;


    public dbca_DataParameter(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public dbca_Function getDbca_function() {
        return dbca_function;
    }

    public void setDbca_function(dbca_Function dbca_function) {
        this.dbca_function = dbca_function;
    }

}






import java.util.List;
import java.util.ArrayList;

public class sqlmodel_datatypes_Domain extends DistinctUserDefinedType {

    private String defaultValue;



    public sqlmodel_datatypes_Domain(
        String defaultValue    ) {
        super(
        );
        this.defaultValue = defaultValue;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }


}
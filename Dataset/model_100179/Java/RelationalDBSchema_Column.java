





import java.util.List;
import java.util.ArrayList;

public class RelationalDBSchema_Column extends NamedElement {

    private String null;
    private String dataType;
    private String defaultValue;



    public RelationalDBSchema_Column(
        String null,        String dataType,        String defaultValue    ) {
        super(
        );
        this.null = null;
        this.dataType = dataType;
        this.defaultValue = defaultValue;
    }


    public String getNull() {
        return null;
    }

    public void setNull(String null) {
        this.null = null;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }


}
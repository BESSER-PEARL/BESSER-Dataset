





import java.util.List;
import java.util.ArrayList;

public class MySQL_Column extends NamedElement {

    private String type;
    private String null;
    private String isPrimaryKey;
    private String defaultValue;
    private String comment;



    public MySQL_Column(
        String type,        String null,        String isPrimaryKey,        String defaultValue,        String comment    ) {
        super(
        );
        this.type = type;
        this.null = null;
        this.isPrimaryKey = isPrimaryKey;
        this.defaultValue = defaultValue;
        this.comment = comment;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getNull() {
        return null;
    }

    public void setNull(String null) {
        this.null = null;
    }
    public String getIsprimarykey() {
        return isPrimaryKey;
    }

    public void setIsprimarykey(String isPrimaryKey) {
        this.isPrimaryKey = isPrimaryKey;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}
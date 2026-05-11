





import java.util.List;
import java.util.ArrayList;

public class MySQL_Column extends NamedElement {

    private String comment;
    private String isPrimaryKey;
    private String defaultValue;
    private String type;



    public MySQL_Column(
        String comment,        String isPrimaryKey,        String defaultValue,        String type    ) {
        super(
        );
        this.comment = comment;
        this.isPrimaryKey = isPrimaryKey;
        this.defaultValue = defaultValue;
        this.type = type;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}
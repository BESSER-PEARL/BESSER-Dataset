





import java.util.List;
import java.util.ArrayList;

public class rdb_Column  {

    private String field;
    private String default;
    private String comment;
    private String null;
    private String type;
    private String key;
    private String logicalField;
    private String extra;



    public rdb_Column(
        String field,        String default,        String comment,        String null,        String type,        String key,        String logicalField,        String extra    ) {
        this.field = field;
        this.default = default;
        this.comment = comment;
        this.null = null;
        this.type = type;
        this.key = key;
        this.logicalField = logicalField;
        this.extra = extra;
    }


    public String getField() {
        return field;
    }

    public void setField(String field) {
        this.field = field;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getNull() {
        return null;
    }

    public void setNull(String null) {
        this.null = null;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getLogicalfield() {
        return logicalField;
    }

    public void setLogicalfield(String logicalField) {
        this.logicalField = logicalField;
    }
    public String getExtra() {
        return extra;
    }

    public void setExtra(String extra) {
        this.extra = extra;
    }


}
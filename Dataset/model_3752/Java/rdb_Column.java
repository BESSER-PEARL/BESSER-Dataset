





import java.util.List;
import java.util.ArrayList;

public class rdb_Column  {

    private String default;
    private String key;
    private String field;
    private String logicalField;
    private String null;
    private String type;
    private String comment;
    private String extra;



    public rdb_Column(
        String default,        String key,        String field,        String logicalField,        String null,        String type,        String comment,        String extra    ) {
        this.default = default;
        this.key = key;
        this.field = field;
        this.logicalField = logicalField;
        this.null = null;
        this.type = type;
        this.comment = comment;
        this.extra = extra;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getField() {
        return field;
    }

    public void setField(String field) {
        this.field = field;
    }
    public String getLogicalfield() {
        return logicalField;
    }

    public void setLogicalfield(String logicalField) {
        this.logicalField = logicalField;
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
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getExtra() {
        return extra;
    }

    public void setExtra(String extra) {
        this.extra = extra;
    }


}
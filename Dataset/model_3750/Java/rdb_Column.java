





import java.util.List;
import java.util.ArrayList;

public class rdb_Column  {

    private String extra;
    private String type;
    private String comment;
    private String field;
    private String default;
    private String logicalField;
    private String null;
    private String key;





    private rdb_Table rdb_table;




    private rdb_Table rdb_table;


    public rdb_Column(
        String extra,        String type,        String comment,        String field,        String default,        String logicalField,        String null,        String key    ) {
        this.extra = extra;
        this.type = type;
        this.comment = comment;
        this.field = field;
        this.default = default;
        this.logicalField = logicalField;
        this.null = null;
        this.key = key;
    }


    public String getExtra() {
        return extra;
    }

    public void setExtra(String extra) {
        this.extra = extra;
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
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public rdb_Table getRdb_table() {
        return rdb_table;
    }

    public void setRdb_table(rdb_Table rdb_table) {
        this.rdb_table = rdb_table;
    }
    public rdb_Table getRdb_table() {
        return rdb_table;
    }

    public void setRdb_table(rdb_Table rdb_table) {
        this.rdb_table = rdb_table;
    }

}
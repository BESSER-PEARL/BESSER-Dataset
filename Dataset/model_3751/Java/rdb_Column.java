





import java.util.List;
import java.util.ArrayList;

public class rdb_Column  {

    private String extra;
    private String logicalField;
    private String default;
    private String null;
    private String type;
    private String key;
    private String comment;
    private String field;





    private rdb_Table rdb_table;




    private rdb_Table rdb_table;


    public rdb_Column(
        String extra,        String logicalField,        String default,        String null,        String type,        String key,        String comment,        String field    ) {
        this.extra = extra;
        this.logicalField = logicalField;
        this.default = default;
        this.null = null;
        this.type = type;
        this.key = key;
        this.comment = comment;
        this.field = field;
    }


    public String getExtra() {
        return extra;
    }

    public void setExtra(String extra) {
        this.extra = extra;
    }
    public String getLogicalfield() {
        return logicalField;
    }

    public void setLogicalfield(String logicalField) {
        this.logicalField = logicalField;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
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
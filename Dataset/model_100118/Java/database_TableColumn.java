





import java.util.List;
import java.util.ArrayList;

public class database_TableColumn extends ExtensibleModel {

    private String fieldName;
    private String chineseName;
    private String columnName;
    private boolean unique;
    private String comments;
    private boolean nullable;
    private String description;
    private String defaultValue;
    private String mark;
    private String columnType;
    private String dataType;
    private boolean primaryKey;
    private String name;





    private database_TableResourceData database_tableresourcedata;


    public database_TableColumn(
        String fieldName,        String chineseName,        String columnName,        boolean unique,        String comments,        boolean nullable,        String description,        String defaultValue,        String mark,        String columnType,        String dataType,        boolean primaryKey,        String name    ) {
        super(
        );
        this.fieldName = fieldName;
        this.chineseName = chineseName;
        this.columnName = columnName;
        this.unique = unique;
        this.comments = comments;
        this.nullable = nullable;
        this.description = description;
        this.defaultValue = defaultValue;
        this.mark = mark;
        this.columnType = columnType;
        this.dataType = dataType;
        this.primaryKey = primaryKey;
        this.name = name;
    }


    public String getFieldname() {
        return fieldName;
    }

    public void setFieldname(String fieldName) {
        this.fieldName = fieldName;
    }
    public String getChinesename() {
        return chineseName;
    }

    public void setChinesename(String chineseName) {
        this.chineseName = chineseName;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getMark() {
        return mark;
    }

    public void setMark(String mark) {
        this.mark = mark;
    }
    public String getColumntype() {
        return columnType;
    }

    public void setColumntype(String columnType) {
        this.columnType = columnType;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public boolean getPrimarykey() {
        return primaryKey;
    }

    public void setPrimarykey(boolean primaryKey) {
        this.primaryKey = primaryKey;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public database_TableResourceData getDatabase_tableresourcedata() {
        return database_tableresourcedata;
    }

    public void setDatabase_tableresourcedata(database_TableResourceData database_tableresourcedata) {
        this.database_tableresourcedata = database_tableresourcedata;
    }

}






import java.util.List;
import java.util.ArrayList;

public class connection_relational_TdSqlDataType  {

    private String localTypeName;
    private String unsignedAttribute;
    private String nullable;
    private int javaDataType;
    private String searchable;
    private String autoIncrement;
    private String caseSensitive;



    public connection_relational_TdSqlDataType(
        String localTypeName,        String unsignedAttribute,        String nullable,        int javaDataType,        String searchable,        String autoIncrement,        String caseSensitive    ) {
        this.localTypeName = localTypeName;
        this.unsignedAttribute = unsignedAttribute;
        this.nullable = nullable;
        this.javaDataType = javaDataType;
        this.searchable = searchable;
        this.autoIncrement = autoIncrement;
        this.caseSensitive = caseSensitive;
    }


    public String getLocaltypename() {
        return localTypeName;
    }

    public void setLocaltypename(String localTypeName) {
        this.localTypeName = localTypeName;
    }
    public String getUnsignedattribute() {
        return unsignedAttribute;
    }

    public void setUnsignedattribute(String unsignedAttribute) {
        this.unsignedAttribute = unsignedAttribute;
    }
    public String getNullable() {
        return nullable;
    }

    public void setNullable(String nullable) {
        this.nullable = nullable;
    }
    public int getJavadatatype() {
        return javaDataType;
    }

    public void setJavadatatype(int javaDataType) {
        this.javaDataType = javaDataType;
    }
    public String getSearchable() {
        return searchable;
    }

    public void setSearchable(String searchable) {
        this.searchable = searchable;
    }
    public String getAutoincrement() {
        return autoIncrement;
    }

    public void setAutoincrement(String autoIncrement) {
        this.autoIncrement = autoIncrement;
    }
    public String getCasesensitive() {
        return caseSensitive;
    }

    public void setCasesensitive(String caseSensitive) {
        this.caseSensitive = caseSensitive;
    }


}
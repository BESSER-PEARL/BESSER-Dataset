





import java.util.List;
import java.util.ArrayList;

public class connection_relational_TdSqlDataType extends SQLSimpleType {

    private String caseSensitive;
    private String nullable;
    private int javaDataType;
    private String unsignedAttribute;
    private String localTypeName;
    private String autoIncrement;
    private String searchable;



    public connection_relational_TdSqlDataType(
        String caseSensitive,        String nullable,        int javaDataType,        String unsignedAttribute,        String localTypeName,        String autoIncrement,        String searchable    ) {
        super(
        );
        this.caseSensitive = caseSensitive;
        this.nullable = nullable;
        this.javaDataType = javaDataType;
        this.unsignedAttribute = unsignedAttribute;
        this.localTypeName = localTypeName;
        this.autoIncrement = autoIncrement;
        this.searchable = searchable;
    }


    public String getCasesensitive() {
        return caseSensitive;
    }

    public void setCasesensitive(String caseSensitive) {
        this.caseSensitive = caseSensitive;
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
    public String getUnsignedattribute() {
        return unsignedAttribute;
    }

    public void setUnsignedattribute(String unsignedAttribute) {
        this.unsignedAttribute = unsignedAttribute;
    }
    public String getLocaltypename() {
        return localTypeName;
    }

    public void setLocaltypename(String localTypeName) {
        this.localTypeName = localTypeName;
    }
    public String getAutoincrement() {
        return autoIncrement;
    }

    public void setAutoincrement(String autoIncrement) {
        this.autoIncrement = autoIncrement;
    }
    public String getSearchable() {
        return searchable;
    }

    public void setSearchable(String searchable) {
        this.searchable = searchable;
    }


}
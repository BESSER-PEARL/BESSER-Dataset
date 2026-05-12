





import java.util.List;
import java.util.ArrayList;

public class connection_relational_TdSqlDataType extends SQLSimpleType {

    private String localTypeName;
    private int javaDataType;
    private String searchable;
    private String caseSensitive;
    private String nullable;
    private String autoIncrement;
    private String unsignedAttribute;



    public connection_relational_TdSqlDataType(
        String localTypeName,        int javaDataType,        String searchable,        String caseSensitive,        String nullable,        String autoIncrement,        String unsignedAttribute    ) {
        super(
        );
        this.localTypeName = localTypeName;
        this.javaDataType = javaDataType;
        this.searchable = searchable;
        this.caseSensitive = caseSensitive;
        this.nullable = nullable;
        this.autoIncrement = autoIncrement;
        this.unsignedAttribute = unsignedAttribute;
    }


    public String getLocaltypename() {
        return localTypeName;
    }

    public void setLocaltypename(String localTypeName) {
        this.localTypeName = localTypeName;
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
    public String getAutoincrement() {
        return autoIncrement;
    }

    public void setAutoincrement(String autoIncrement) {
        this.autoIncrement = autoIncrement;
    }
    public String getUnsignedattribute() {
        return unsignedAttribute;
    }

    public void setUnsignedattribute(String unsignedAttribute) {
        this.unsignedAttribute = unsignedAttribute;
    }


}
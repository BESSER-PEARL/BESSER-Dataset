





import java.util.List;
import java.util.ArrayList;

public class cwm_relational_TdSqlDataType extends SQLSimpleType {

    private String unsignedAttribute;
    private String searchable;
    private String nullable;
    private String caseSensitive;
    private int javaDataType;
    private String autoIncrement;
    private String localTypeName;



    public cwm_relational_TdSqlDataType(
        String unsignedAttribute,        String searchable,        String nullable,        String caseSensitive,        int javaDataType,        String autoIncrement,        String localTypeName    ) {
        super(
        );
        this.unsignedAttribute = unsignedAttribute;
        this.searchable = searchable;
        this.nullable = nullable;
        this.caseSensitive = caseSensitive;
        this.javaDataType = javaDataType;
        this.autoIncrement = autoIncrement;
        this.localTypeName = localTypeName;
    }


    public String getUnsignedattribute() {
        return unsignedAttribute;
    }

    public void setUnsignedattribute(String unsignedAttribute) {
        this.unsignedAttribute = unsignedAttribute;
    }
    public String getSearchable() {
        return searchable;
    }

    public void setSearchable(String searchable) {
        this.searchable = searchable;
    }
    public String getNullable() {
        return nullable;
    }

    public void setNullable(String nullable) {
        this.nullable = nullable;
    }
    public String getCasesensitive() {
        return caseSensitive;
    }

    public void setCasesensitive(String caseSensitive) {
        this.caseSensitive = caseSensitive;
    }
    public int getJavadatatype() {
        return javaDataType;
    }

    public void setJavadatatype(int javaDataType) {
        this.javaDataType = javaDataType;
    }
    public String getAutoincrement() {
        return autoIncrement;
    }

    public void setAutoincrement(String autoIncrement) {
        this.autoIncrement = autoIncrement;
    }
    public String getLocaltypename() {
        return localTypeName;
    }

    public void setLocaltypename(String localTypeName) {
        this.localTypeName = localTypeName;
    }


}
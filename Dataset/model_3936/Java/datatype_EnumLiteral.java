





import java.util.List;
import java.util.ArrayList;

public class datatype_EnumLiteral  {

    private String name;
    private String description;





    private datatype_Enum datatype_enum;




    private datatype_EnumLiteralPropertyAttribute datatype_enumliteralpropertyattribute;


    public datatype_EnumLiteral(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public datatype_Enum getDatatype_enum() {
        return datatype_enum;
    }

    public void setDatatype_enum(datatype_Enum datatype_enum) {
        this.datatype_enum = datatype_enum;
    }
    public datatype_EnumLiteralPropertyAttribute getDatatype_enumliteralpropertyattribute() {
        return datatype_enumliteralpropertyattribute;
    }

    public void setDatatype_enumliteralpropertyattribute(datatype_EnumLiteralPropertyAttribute datatype_enumliteralpropertyattribute) {
        this.datatype_enumliteralpropertyattribute = datatype_enumliteralpropertyattribute;
    }

}
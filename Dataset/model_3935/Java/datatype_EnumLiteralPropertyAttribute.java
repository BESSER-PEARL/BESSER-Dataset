





import java.util.List;
import java.util.ArrayList;

public class datatype_EnumLiteralPropertyAttribute extends PropertyAttribute {

    private String type;





    private datatype_EnumLiteral datatype_enumliteral;


    public datatype_EnumLiteralPropertyAttribute(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public datatype_EnumLiteral getDatatype_enumliteral() {
        return datatype_enumliteral;
    }

    public void setDatatype_enumliteral(datatype_EnumLiteral datatype_enumliteral) {
        this.datatype_enumliteral = datatype_enumliteral;
    }

}
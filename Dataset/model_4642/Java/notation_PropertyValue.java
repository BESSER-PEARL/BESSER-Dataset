





import java.util.List;
import java.util.ArrayList;

public class notation_PropertyValue extends StringObjectConverter {

    private String rawValue;





    private notation_EDataType notation_edatatype;




    private notation_StringToPropertyValueMapEntry notation_stringtopropertyvaluemapentry;


    public notation_PropertyValue(
        String rawValue    ) {
        super(
        );
        this.rawValue = rawValue;
    }


    public String getRawvalue() {
        return rawValue;
    }

    public void setRawvalue(String rawValue) {
        this.rawValue = rawValue;
    }

    public notation_EDataType getNotation_edatatype() {
        return notation_edatatype;
    }

    public void setNotation_edatatype(notation_EDataType notation_edatatype) {
        this.notation_edatatype = notation_edatatype;
    }
    public notation_StringToPropertyValueMapEntry getNotation_stringtopropertyvaluemapentry() {
        return notation_stringtopropertyvaluemapentry;
    }

    public void setNotation_stringtopropertyvaluemapentry(notation_StringToPropertyValueMapEntry notation_stringtopropertyvaluemapentry) {
        this.notation_stringtopropertyvaluemapentry = notation_stringtopropertyvaluemapentry;
    }

}
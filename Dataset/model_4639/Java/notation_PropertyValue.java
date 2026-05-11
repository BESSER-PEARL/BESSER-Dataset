





import java.util.List;
import java.util.ArrayList;

public class notation_PropertyValue extends StringObjectConverter {

    private String rawValue;





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

    public notation_StringToPropertyValueMapEntry getNotation_stringtopropertyvaluemapentry() {
        return notation_stringtopropertyvaluemapentry;
    }

    public void setNotation_stringtopropertyvaluemapentry(notation_StringToPropertyValueMapEntry notation_stringtopropertyvaluemapentry) {
        this.notation_stringtopropertyvaluemapentry = notation_stringtopropertyvaluemapentry;
    }

}






import java.util.List;
import java.util.ArrayList;

public class notation_PropertiesSetStyle extends NamedStyle {






    private List<notation_StringToPropertyValueMapEntry> notation_stringtopropertyvaluemapentrys;


    public notation_PropertiesSetStyle(
    ) {
        super(
        );
        this.notation_stringtopropertyvaluemapentrys = new ArrayList<>();
    }

    public notation_PropertiesSetStyle(
        ArrayList<notation_StringToPropertyValueMapEntry> notation_stringtopropertyvaluemapentrys    ) {
        this.notation_stringtopropertyvaluemapentrys = notation_stringtopropertyvaluemapentrys;
    }


    public List<notation_StringToPropertyValueMapEntry> getNotation_stringtopropertyvaluemapentrys() {
        return notation_stringtopropertyvaluemapentrys;
    }

    public void addNotation_stringtopropertyvaluemapentry(Notation_stringtopropertyvaluemapentry notation_stringtopropertyvaluemapentry) {
        this.notation_stringtopropertyvaluemapentrys.add(notation_stringtopropertyvaluemapentry);
    }

}






import java.util.List;
import java.util.ArrayList;

public class VisualInterface_StringToStringMap  {

    private String key;
    private String value;





    private VisualInterface_SymbolReference visualinterface_symbolreference;




    private VisualInterface_Symbol visualinterface_symbol;


    public VisualInterface_StringToStringMap(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public VisualInterface_SymbolReference getVisualinterface_symbolreference() {
        return visualinterface_symbolreference;
    }

    public void setVisualinterface_symbolreference(VisualInterface_SymbolReference visualinterface_symbolreference) {
        this.visualinterface_symbolreference = visualinterface_symbolreference;
    }
    public VisualInterface_Symbol getVisualinterface_symbol() {
        return visualinterface_symbol;
    }

    public void setVisualinterface_symbol(VisualInterface_Symbol visualinterface_symbol) {
        this.visualinterface_symbol = visualinterface_symbol;
    }

}






import java.util.List;
import java.util.ArrayList;

public class model_StringToStringMap  {

    private String value;
    private String key;





    private model_SymbolReference model_symbolreference;




    private model_Symbol model_symbol;


    public model_StringToStringMap(
        String value,        String key    ) {
        this.value = value;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public model_SymbolReference getModel_symbolreference() {
        return model_symbolreference;
    }

    public void setModel_symbolreference(model_SymbolReference model_symbolreference) {
        this.model_symbolreference = model_symbolreference;
    }
    public model_Symbol getModel_symbol() {
        return model_symbol;
    }

    public void setModel_symbol(model_Symbol model_symbol) {
        this.model_symbol = model_symbol;
    }

}
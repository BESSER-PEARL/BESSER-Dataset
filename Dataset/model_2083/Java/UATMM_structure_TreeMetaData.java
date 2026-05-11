





import java.util.List;
import java.util.ArrayList;

public class UATMM_structure_TreeMetaData  {

    private String Value;
    private String Key;



    public UATMM_structure_TreeMetaData(
        String Value,        String Key    ) {
        this.Value = Value;
        this.Key = Key;
    }


    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getKey() {
        return Key;
    }

    public void setKey(String Key) {
        this.Key = Key;
    }


}
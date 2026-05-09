





import java.util.List;
import java.util.ArrayList;

public class MARTE_Library_BasicNFP_Types_NFP_String extends NFP_CommonType {

    private String value;



    public MARTE_Library_BasicNFP_Types_NFP_String(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}
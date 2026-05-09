





import java.util.List;
import java.util.ArrayList;

public class rif12_ExchangeFile_DatatypeDefinitionString extends DatatypeDefinitionSimple {

    private String maxLength;



    public rif12_ExchangeFile_DatatypeDefinitionString(
        String maxLength    ) {
        super(
        );
        this.maxLength = maxLength;
    }


    public String getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(String maxLength) {
        this.maxLength = maxLength;
    }


}
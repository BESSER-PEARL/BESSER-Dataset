





import java.util.List;
import java.util.ArrayList;

public class XHTML_Param extends ObjectElement, EMPTY {

    private String valuetype;



    public XHTML_Param(
        String valuetype    ) {
        super(
        );
        this.valuetype = valuetype;
    }


    public String getValuetype() {
        return valuetype;
    }

    public void setValuetype(String valuetype) {
        this.valuetype = valuetype;
    }


}
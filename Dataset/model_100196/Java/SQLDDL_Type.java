





import java.util.List;
import java.util.ArrayList;

public class SQLDDL_Type extends NamedElement {

    private String length;
    private String isUnsigned;



    public SQLDDL_Type(
        String length,        String isUnsigned    ) {
        super(
        );
        this.length = length;
        this.isUnsigned = isUnsigned;
    }


    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }
    public String getIsunsigned() {
        return isUnsigned;
    }

    public void setIsunsigned(String isUnsigned) {
        this.isUnsigned = isUnsigned;
    }


}
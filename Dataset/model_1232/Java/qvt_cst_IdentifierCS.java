





import java.util.List;
import java.util.ArrayList;

public class qvt_cst_IdentifierCS extends cst_IHasName, cst_CSTNode {

    private String value;



    public qvt_cst_IdentifierCS(
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
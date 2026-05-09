





import java.util.List;
import java.util.ArrayList;

public class org_structure_Using extends KermetaModelElement {

    private String fromQName;
    private String toName;



    public org_structure_Using(
        String fromQName,        String toName    ) {
        super(
        );
        this.fromQName = fromQName;
        this.toName = toName;
    }


    public String getFromqname() {
        return fromQName;
    }

    public void setFromqname(String fromQName) {
        this.fromQName = fromQName;
    }
    public String getToname() {
        return toName;
    }

    public void setToname(String toName) {
        this.toName = toName;
    }


}
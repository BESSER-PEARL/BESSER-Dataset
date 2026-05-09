





import java.util.List;
import java.util.ArrayList;

public class org_structure_Using extends KermetaModelElement {

    private String toName;
    private String fromQName;



    public org_structure_Using(
        String toName,        String fromQName    ) {
        super(
        );
        this.toName = toName;
        this.fromQName = fromQName;
    }


    public String getToname() {
        return toName;
    }

    public void setToname(String toName) {
        this.toName = toName;
    }
    public String getFromqname() {
        return fromQName;
    }

    public void setFromqname(String fromQName) {
        this.fromQName = fromQName;
    }


}
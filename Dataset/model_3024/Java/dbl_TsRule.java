





import java.util.List;
import java.util.ArrayList;

public class dbl_TsRule extends NamedElement, ReferableRhsType {

    private String metaClassName;



    public dbl_TsRule(
        String metaClassName    ) {
        super(
        );
        this.metaClassName = metaClassName;
    }


    public String getMetaclassname() {
        return metaClassName;
    }

    public void setMetaclassname(String metaClassName) {
        this.metaClassName = metaClassName;
    }


}






import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_EnumDataBinding extends DataBinding {

    private String enumClassName;



    public appBuilderDSL_EnumDataBinding(
        String enumClassName    ) {
        super(
        );
        this.enumClassName = enumClassName;
    }


    public String getEnumclassname() {
        return enumClassName;
    }

    public void setEnumclassname(String enumClassName) {
        this.enumClassName = enumClassName;
    }


}
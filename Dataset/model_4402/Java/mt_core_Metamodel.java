





import java.util.List;
import java.util.ArrayList;

public class mt_core_Metamodel extends Resource {

    private String packageClass;



    public mt_core_Metamodel(
        String packageClass    ) {
        super(
        );
        this.packageClass = packageClass;
    }


    public String getPackageclass() {
        return packageClass;
    }

    public void setPackageclass(String packageClass) {
        this.packageClass = packageClass;
    }


}






import java.util.List;
import java.util.ArrayList;

public class mMDSL_Reference  {

    private String name;





    private mMDSL_Class mmdsl_class;


    public mMDSL_Reference(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mMDSL_Class getMmdsl_class() {
        return mmdsl_class;
    }

    public void setMmdsl_class(mMDSL_Class mmdsl_class) {
        this.mmdsl_class = mmdsl_class;
    }

}
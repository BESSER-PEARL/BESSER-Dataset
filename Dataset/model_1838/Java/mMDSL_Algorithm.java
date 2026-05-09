





import java.util.List;
import java.util.ArrayList;

public class mMDSL_Algorithm  {

    private String name;





    private mMDSL_Method mmdsl_method;


    public mMDSL_Algorithm(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mMDSL_Method getMmdsl_method() {
        return mmdsl_method;
    }

    public void setMmdsl_method(mMDSL_Method mmdsl_method) {
        this.mmdsl_method = mmdsl_method;
    }

}
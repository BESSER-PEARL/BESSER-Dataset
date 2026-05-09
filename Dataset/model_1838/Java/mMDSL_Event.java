





import java.util.List;
import java.util.ArrayList;

public class mMDSL_Event  {

    private String name;





    private mMDSL_Method mmdsl_method;




    private mMDSL_Algorithm mmdsl_algorithm;


    public mMDSL_Event(
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
    public mMDSL_Algorithm getMmdsl_algorithm() {
        return mmdsl_algorithm;
    }

    public void setMmdsl_algorithm(mMDSL_Algorithm mmdsl_algorithm) {
        this.mmdsl_algorithm = mmdsl_algorithm;
    }

}
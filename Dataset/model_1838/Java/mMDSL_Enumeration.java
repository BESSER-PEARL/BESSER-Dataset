





import java.util.List;
import java.util.ArrayList;

public class mMDSL_Enumeration  {

    private String name;
    private String enumvalues;





    private mMDSL_Method mmdsl_method;


    public mMDSL_Enumeration(
        String name,        String enumvalues    ) {
        this.name = name;
        this.enumvalues = enumvalues;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEnumvalues() {
        return enumvalues;
    }

    public void setEnumvalues(String enumvalues) {
        this.enumvalues = enumvalues;
    }

    public mMDSL_Method getMmdsl_method() {
        return mmdsl_method;
    }

    public void setMmdsl_method(mMDSL_Method mmdsl_method) {
        this.mmdsl_method = mmdsl_method;
    }

}
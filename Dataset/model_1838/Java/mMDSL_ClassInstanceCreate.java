





import java.util.List;
import java.util.ArrayList;

public class mMDSL_ClassInstanceCreate  {

    private String name;





    private mMDSL_ClassInstance mmdsl_classinstance;




    private mMDSL_Class mmdsl_class;


    public mMDSL_ClassInstanceCreate(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mMDSL_ClassInstance getMmdsl_classinstance() {
        return mmdsl_classinstance;
    }

    public void setMmdsl_classinstance(mMDSL_ClassInstance mmdsl_classinstance) {
        this.mmdsl_classinstance = mmdsl_classinstance;
    }
    public mMDSL_Class getMmdsl_class() {
        return mmdsl_class;
    }

    public void setMmdsl_class(mMDSL_Class mmdsl_class) {
        this.mmdsl_class = mmdsl_class;
    }

}






import java.util.List;
import java.util.ArrayList;

public class jbatch_ExcludeType  {

    private String class_;





    private jbatch_ExceptionClassFilter jbatch_exceptionclassfilter;


    public jbatch_ExcludeType(
        String class_    ) {
        this.class_ = class_;
    }


    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }

    public jbatch_ExceptionClassFilter getJbatch_exceptionclassfilter() {
        return jbatch_exceptionclassfilter;
    }

    public void setJbatch_exceptionclassfilter(jbatch_ExceptionClassFilter jbatch_exceptionclassfilter) {
        this.jbatch_exceptionclassfilter = jbatch_exceptionclassfilter;
    }

}
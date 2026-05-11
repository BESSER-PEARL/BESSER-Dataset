





import java.util.List;
import java.util.ArrayList;

public class tExp_Role  {

    private String name;
    private String class_;
    private String args;





    private tExp_TraceExpression texp_traceexpression;


    public tExp_Role(
        String name,        String class_,        String args    ) {
        this.name = name;
        this.class_ = class_;
        this.args = args;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getArgs() {
        return args;
    }

    public void setArgs(String args) {
        this.args = args;
    }

    public tExp_TraceExpression getTexp_traceexpression() {
        return texp_traceexpression;
    }

    public void setTexp_traceexpression(tExp_TraceExpression texp_traceexpression) {
        this.texp_traceexpression = texp_traceexpression;
    }

}






import java.util.List;
import java.util.ArrayList;

public class org_behavior_JavaStaticCall extends Expression {

    private String jclass;
    private String jmethod;



    public org_behavior_JavaStaticCall(
        String jclass,        String jmethod    ) {
        super(
        );
        this.jclass = jclass;
        this.jmethod = jmethod;
    }


    public String getJclass() {
        return jclass;
    }

    public void setJclass(String jclass) {
        this.jclass = jclass;
    }
    public String getJmethod() {
        return jmethod;
    }

    public void setJmethod(String jmethod) {
        this.jmethod = jmethod;
    }


}
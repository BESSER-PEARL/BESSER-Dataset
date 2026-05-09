





import java.util.List;
import java.util.ArrayList;

public class kermeta_behavior_JavaStaticCall extends Expression {

    private String jmethod;
    private String jclass;



    public kermeta_behavior_JavaStaticCall(
        String jmethod,        String jclass    ) {
        super(
        );
        this.jmethod = jmethod;
        this.jclass = jclass;
    }


    public String getJmethod() {
        return jmethod;
    }

    public void setJmethod(String jmethod) {
        this.jmethod = jmethod;
    }
    public String getJclass() {
        return jclass;
    }

    public void setJclass(String jclass) {
        this.jclass = jclass;
    }


}
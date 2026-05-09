





import java.util.List;
import java.util.ArrayList;

public class jbatch_Batchlet  {

    private String ref;





    private jbatch_Step jbatch_step;




    private jbatch_Properties jbatch_properties;


    public jbatch_Batchlet(
        String ref    ) {
        this.ref = ref;
    }


    public String getRef() {
        return ref;
    }

    public void setRef(String ref) {
        this.ref = ref;
    }

    public jbatch_Step getJbatch_step() {
        return jbatch_step;
    }

    public void setJbatch_step(jbatch_Step jbatch_step) {
        this.jbatch_step = jbatch_step;
    }
    public jbatch_Properties getJbatch_properties() {
        return jbatch_properties;
    }

    public void setJbatch_properties(jbatch_Properties jbatch_properties) {
        this.jbatch_properties = jbatch_properties;
    }

}
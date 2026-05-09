





import java.util.List;
import java.util.ArrayList;

public class jbatch_Collector  {

    private String ref;





    private jbatch_Partition jbatch_partition;




    private jbatch_Properties jbatch_properties;


    public jbatch_Collector(
        String ref    ) {
        this.ref = ref;
    }


    public String getRef() {
        return ref;
    }

    public void setRef(String ref) {
        this.ref = ref;
    }

    public jbatch_Partition getJbatch_partition() {
        return jbatch_partition;
    }

    public void setJbatch_partition(jbatch_Partition jbatch_partition) {
        this.jbatch_partition = jbatch_partition;
    }
    public jbatch_Properties getJbatch_properties() {
        return jbatch_properties;
    }

    public void setJbatch_properties(jbatch_Properties jbatch_properties) {
        this.jbatch_properties = jbatch_properties;
    }

}






import java.util.List;
import java.util.ArrayList;

public class jbatch_PartitionReducer  {

    private String ref;





    private jbatch_Partition jbatch_partition;


    public jbatch_PartitionReducer(
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

}
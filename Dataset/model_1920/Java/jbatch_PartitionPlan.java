





import java.util.List;
import java.util.ArrayList;

public class jbatch_PartitionPlan  {

    private String threads;
    private String partitions;





    private jbatch_Partition jbatch_partition;


    public jbatch_PartitionPlan(
        String threads,        String partitions    ) {
        this.threads = threads;
        this.partitions = partitions;
    }


    public String getThreads() {
        return threads;
    }

    public void setThreads(String threads) {
        this.threads = threads;
    }
    public String getPartitions() {
        return partitions;
    }

    public void setPartitions(String partitions) {
        this.partitions = partitions;
    }

    public jbatch_Partition getJbatch_partition() {
        return jbatch_partition;
    }

    public void setJbatch_partition(jbatch_Partition jbatch_partition) {
        this.jbatch_partition = jbatch_partition;
    }

}
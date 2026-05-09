





import java.util.List;
import java.util.ArrayList;

public class jbatch_Chunk  {

    private String retryLimit;
    private String skipLimit;
    private String timeLimit;
    private String checkpointPolicy;
    private String itemCount;





    private jbatch_CheckpointAlgorithm jbatch_checkpointalgorithm;




    private jbatch_Step jbatch_step;


    public jbatch_Chunk(
        String retryLimit,        String skipLimit,        String timeLimit,        String checkpointPolicy,        String itemCount    ) {
        this.retryLimit = retryLimit;
        this.skipLimit = skipLimit;
        this.timeLimit = timeLimit;
        this.checkpointPolicy = checkpointPolicy;
        this.itemCount = itemCount;
    }


    public String getRetrylimit() {
        return retryLimit;
    }

    public void setRetrylimit(String retryLimit) {
        this.retryLimit = retryLimit;
    }
    public String getSkiplimit() {
        return skipLimit;
    }

    public void setSkiplimit(String skipLimit) {
        this.skipLimit = skipLimit;
    }
    public String getTimelimit() {
        return timeLimit;
    }

    public void setTimelimit(String timeLimit) {
        this.timeLimit = timeLimit;
    }
    public String getCheckpointpolicy() {
        return checkpointPolicy;
    }

    public void setCheckpointpolicy(String checkpointPolicy) {
        this.checkpointPolicy = checkpointPolicy;
    }
    public String getItemcount() {
        return itemCount;
    }

    public void setItemcount(String itemCount) {
        this.itemCount = itemCount;
    }

    public jbatch_CheckpointAlgorithm getJbatch_checkpointalgorithm() {
        return jbatch_checkpointalgorithm;
    }

    public void setJbatch_checkpointalgorithm(jbatch_CheckpointAlgorithm jbatch_checkpointalgorithm) {
        this.jbatch_checkpointalgorithm = jbatch_checkpointalgorithm;
    }
    public jbatch_Step getJbatch_step() {
        return jbatch_step;
    }

    public void setJbatch_step(jbatch_Step jbatch_step) {
        this.jbatch_step = jbatch_step;
    }

}
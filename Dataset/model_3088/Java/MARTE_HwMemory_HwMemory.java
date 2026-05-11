





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwMemory_HwMemory extends HwGeneral_HwResource, GRM_StorageResource {

    private String throughput;
    private String timings;
    private String adressSize;
    private String memorySize;



    public MARTE_HwMemory_HwMemory(
        String throughput,        String timings,        String adressSize,        String memorySize    ) {
        super(
        );
        this.throughput = throughput;
        this.timings = timings;
        this.adressSize = adressSize;
        this.memorySize = memorySize;
    }


    public String getThroughput() {
        return throughput;
    }

    public void setThroughput(String throughput) {
        this.throughput = throughput;
    }
    public String getTimings() {
        return timings;
    }

    public void setTimings(String timings) {
        this.timings = timings;
    }
    public String getAdresssize() {
        return adressSize;
    }

    public void setAdresssize(String adressSize) {
        this.adressSize = adressSize;
    }
    public String getMemorysize() {
        return memorySize;
    }

    public void setMemorysize(String memorySize) {
        this.memorySize = memorySize;
    }


}
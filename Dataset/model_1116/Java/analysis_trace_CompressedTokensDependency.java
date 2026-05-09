





import java.util.List;
import java.util.ArrayList;

public class analysis_trace_CompressedTokensDependency extends CompressedDependency {






    private List<BufferToStatisticalDataMap> buffertostatisticaldatamaps;


    public analysis_trace_CompressedTokensDependency(
    ) {
        super(
        );
        this.buffertostatisticaldatamaps = new ArrayList<>();
    }

    public analysis_trace_CompressedTokensDependency(
        ArrayList<BufferToStatisticalDataMap> buffertostatisticaldatamaps    ) {
        this.buffertostatisticaldatamaps = buffertostatisticaldatamaps;
    }


    public List<BufferToStatisticalDataMap> getBuffertostatisticaldatamaps() {
        return buffertostatisticaldatamaps;
    }

    public void addBuffertostatisticaldatamap(Buffertostatisticaldatamap buffertostatisticaldatamap) {
        this.buffertostatisticaldatamaps.add(buffertostatisticaldatamap);
    }

}
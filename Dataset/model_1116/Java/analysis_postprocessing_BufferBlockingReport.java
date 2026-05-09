





import java.util.List;
import java.util.ArrayList;

public class analysis_postprocessing_BufferBlockingReport extends PostProcessingData {






    private List<BufferToDoubleMap> buffertodoublemaps;




    private postprocessing_analysis_Network postprocessing_analysis_network;




    private List<BufferToIntegerMap> buffertointegermaps;




    private List<BufferToIntegerMap> buffertointegermaps;


    public analysis_postprocessing_BufferBlockingReport(
    ) {
        super(
        );
        this.buffertodoublemaps = new ArrayList<>();
        this.buffertointegermaps = new ArrayList<>();
        this.buffertointegermaps = new ArrayList<>();
    }

    public analysis_postprocessing_BufferBlockingReport(
        ArrayList<BufferToDoubleMap> buffertodoublemaps,        ArrayList<BufferToIntegerMap> buffertointegermaps,        ArrayList<BufferToIntegerMap> buffertointegermaps    ) {
        this.buffertodoublemaps = buffertodoublemaps;
        this.buffertointegermaps = buffertointegermaps;
        this.buffertointegermaps = buffertointegermaps;
    }


    public List<BufferToDoubleMap> getBuffertodoublemaps() {
        return buffertodoublemaps;
    }

    public void addBuffertodoublemap(Buffertodoublemap buffertodoublemap) {
        this.buffertodoublemaps.add(buffertodoublemap);
    }
    public postprocessing_analysis_Network getPostprocessing_analysis_network() {
        return postprocessing_analysis_network;
    }

    public void setPostprocessing_analysis_network(postprocessing_analysis_Network postprocessing_analysis_network) {
        this.postprocessing_analysis_network = postprocessing_analysis_network;
    }
    public List<BufferToIntegerMap> getBuffertointegermaps() {
        return buffertointegermaps;
    }

    public void addBuffertointegermap(Buffertointegermap buffertointegermap) {
        this.buffertointegermaps.add(buffertointegermap);
    }
    public List<BufferToIntegerMap> getBuffertointegermaps() {
        return buffertointegermaps;
    }

    public void addBuffertointegermap(Buffertointegermap buffertointegermap) {
        this.buffertointegermaps.add(buffertointegermap);
    }

}
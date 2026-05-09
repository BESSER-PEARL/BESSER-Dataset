





import java.util.List;
import java.util.ArrayList;

public class analysis_postprocessing_ActorStatisticsReport extends PostProcessingData {

    private float averageOccupancy;
    private float occupancyDeviation;
    private float executionTime;





    private List<StringToDoubleMap> stringtodoublemaps;




    private List<StringToDoubleMap> stringtodoublemaps;




    private List<StringToDoubleMap> stringtodoublemaps;




    private List<StringToDoubleMap> stringtodoublemaps;




    private postprocessing_analysis_Network postprocessing_analysis_network;


    public analysis_postprocessing_ActorStatisticsReport(
        float averageOccupancy,        float occupancyDeviation,        float executionTime    ) {
        super(
        );
        this.averageOccupancy = averageOccupancy;
        this.occupancyDeviation = occupancyDeviation;
        this.executionTime = executionTime;
        this.stringtodoublemaps = new ArrayList<>();
        this.stringtodoublemaps = new ArrayList<>();
        this.stringtodoublemaps = new ArrayList<>();
        this.stringtodoublemaps = new ArrayList<>();
    }

    public analysis_postprocessing_ActorStatisticsReport(
        float averageOccupancy,        float occupancyDeviation,        float executionTime        ArrayList<StringToDoubleMap> stringtodoublemaps,        ArrayList<StringToDoubleMap> stringtodoublemaps,        ArrayList<StringToDoubleMap> stringtodoublemaps,        ArrayList<StringToDoubleMap> stringtodoublemaps    ) {
        this.averageOccupancy = averageOccupancy;
        this.occupancyDeviation = occupancyDeviation;
        this.executionTime = executionTime;
        this.stringtodoublemaps = stringtodoublemaps;
        this.stringtodoublemaps = stringtodoublemaps;
        this.stringtodoublemaps = stringtodoublemaps;
        this.stringtodoublemaps = stringtodoublemaps;
    }

    public float getAverageoccupancy() {
        return averageOccupancy;
    }

    public void setAverageoccupancy(float averageOccupancy) {
        this.averageOccupancy = averageOccupancy;
    }
    public float getOccupancydeviation() {
        return occupancyDeviation;
    }

    public void setOccupancydeviation(float occupancyDeviation) {
        this.occupancyDeviation = occupancyDeviation;
    }
    public float getExecutiontime() {
        return executionTime;
    }

    public void setExecutiontime(float executionTime) {
        this.executionTime = executionTime;
    }

    public List<StringToDoubleMap> getStringtodoublemaps() {
        return stringtodoublemaps;
    }

    public void addStringtodoublemap(Stringtodoublemap stringtodoublemap) {
        this.stringtodoublemaps.add(stringtodoublemap);
    }
    public List<StringToDoubleMap> getStringtodoublemaps() {
        return stringtodoublemaps;
    }

    public void addStringtodoublemap(Stringtodoublemap stringtodoublemap) {
        this.stringtodoublemaps.add(stringtodoublemap);
    }
    public List<StringToDoubleMap> getStringtodoublemaps() {
        return stringtodoublemaps;
    }

    public void addStringtodoublemap(Stringtodoublemap stringtodoublemap) {
        this.stringtodoublemaps.add(stringtodoublemap);
    }
    public List<StringToDoubleMap> getStringtodoublemaps() {
        return stringtodoublemaps;
    }

    public void addStringtodoublemap(Stringtodoublemap stringtodoublemap) {
        this.stringtodoublemaps.add(stringtodoublemap);
    }
    public postprocessing_analysis_Network getPostprocessing_analysis_network() {
        return postprocessing_analysis_network;
    }

    public void setPostprocessing_analysis_network(postprocessing_analysis_Network postprocessing_analysis_network) {
        this.postprocessing_analysis_network = postprocessing_analysis_network;
    }

}
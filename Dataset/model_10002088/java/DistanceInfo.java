





import java.util.List;
import java.util.ArrayList;

public class DistanceInfo  {

    private String Distaince;
    private String ShortestPath;
    private String TraficInfo;



    public DistanceInfo(
        String Distaince,        String ShortestPath,        String TraficInfo    ) {
        this.Distaince = Distaince;
        this.ShortestPath = ShortestPath;
        this.TraficInfo = TraficInfo;
    }


    public String getDistaince() {
        return Distaince;
    }

    public void setDistaince(String Distaince) {
        this.Distaince = Distaince;
    }
    public String getShortestpath() {
        return ShortestPath;
    }

    public void setShortestpath(String ShortestPath) {
        this.ShortestPath = ShortestPath;
    }
    public String getTraficinfo() {
        return TraficInfo;
    }

    public void setTraficinfo(String TraficInfo) {
        this.TraficInfo = TraficInfo;
    }


}
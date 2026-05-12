





import java.util.List;
import java.util.ArrayList;

public class YasperEPNML114_ConnectionWeight  {

    private String connection;





    private YasperEPNML114_ConnectionWeights yasperepnml114_connectionweights;




    private YasperEPNML114_Stat yasperepnml114_stat;


    public YasperEPNML114_ConnectionWeight(
        String connection    ) {
        this.connection = connection;
    }


    public String getConnection() {
        return connection;
    }

    public void setConnection(String connection) {
        this.connection = connection;
    }

    public YasperEPNML114_ConnectionWeights getYasperepnml114_connectionweights() {
        return yasperepnml114_connectionweights;
    }

    public void setYasperepnml114_connectionweights(YasperEPNML114_ConnectionWeights yasperepnml114_connectionweights) {
        this.yasperepnml114_connectionweights = yasperepnml114_connectionweights;
    }
    public YasperEPNML114_Stat getYasperepnml114_stat() {
        return yasperepnml114_stat;
    }

    public void setYasperepnml114_stat(YasperEPNML114_Stat yasperepnml114_stat) {
        this.yasperepnml114_stat = yasperepnml114_stat;
    }

}






import java.util.List;
import java.util.ArrayList;

public class ddsm_SparkCluster extends MasterSlavePlatform {

    private int sparkExecutorMemory;
    private int driverCores;
    private int UIPort;
    private int driverMemory;
    private int maxResultSize;



    public ddsm_SparkCluster(
        int sparkExecutorMemory,        int driverCores,        int UIPort,        int driverMemory,        int maxResultSize    ) {
        super(
        );
        this.sparkExecutorMemory = sparkExecutorMemory;
        this.driverCores = driverCores;
        this.UIPort = UIPort;
        this.driverMemory = driverMemory;
        this.maxResultSize = maxResultSize;
    }


    public int getSparkexecutormemory() {
        return sparkExecutorMemory;
    }

    public void setSparkexecutormemory(int sparkExecutorMemory) {
        this.sparkExecutorMemory = sparkExecutorMemory;
    }
    public int getDrivercores() {
        return driverCores;
    }

    public void setDrivercores(int driverCores) {
        this.driverCores = driverCores;
    }
    public int getUiport() {
        return UIPort;
    }

    public void setUiport(int UIPort) {
        this.UIPort = UIPort;
    }
    public int getDrivermemory() {
        return driverMemory;
    }

    public void setDrivermemory(int driverMemory) {
        this.driverMemory = driverMemory;
    }
    public int getMaxresultsize() {
        return maxResultSize;
    }

    public void setMaxresultsize(int maxResultSize) {
        this.maxResultSize = maxResultSize;
    }


}
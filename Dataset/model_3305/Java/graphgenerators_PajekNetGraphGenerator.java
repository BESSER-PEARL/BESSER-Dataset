





import java.util.List;
import java.util.ArrayList;

public class graphgenerators_PajekNetGraphGenerator extends GraphGenerator {

    private float area;
    private int colArea;
    private int zoomFactor;
    private String dataFile_net;



    public graphgenerators_PajekNetGraphGenerator(
        float area,        int colArea,        int zoomFactor,        String dataFile_net    ) {
        super(
        );
        this.area = area;
        this.colArea = colArea;
        this.zoomFactor = zoomFactor;
        this.dataFile_net = dataFile_net;
    }


    public float getArea() {
        return area;
    }

    public void setArea(float area) {
        this.area = area;
    }
    public int getColarea() {
        return colArea;
    }

    public void setColarea(int colArea) {
        this.colArea = colArea;
    }
    public int getZoomfactor() {
        return zoomFactor;
    }

    public void setZoomfactor(int zoomFactor) {
        this.zoomFactor = zoomFactor;
    }
    public String getDatafile_net() {
        return dataFile_net;
    }

    public void setDatafile_net(String dataFile_net) {
        this.dataFile_net = dataFile_net;
    }


}






import java.util.List;
import java.util.ArrayList;

public class sedml_curve  {

    private String xDataReference;
    private String logY;
    private String logX;
    private String yDataReference;
    private String id;





    private sedml_listOfCurves sedml_listofcurves;


    public sedml_curve(
        String xDataReference,        String logY,        String logX,        String yDataReference,        String id    ) {
        this.xDataReference = xDataReference;
        this.logY = logY;
        this.logX = logX;
        this.yDataReference = yDataReference;
        this.id = id;
    }


    public String getXdatareference() {
        return xDataReference;
    }

    public void setXdatareference(String xDataReference) {
        this.xDataReference = xDataReference;
    }
    public String getLogy() {
        return logY;
    }

    public void setLogy(String logY) {
        this.logY = logY;
    }
    public String getLogx() {
        return logX;
    }

    public void setLogx(String logX) {
        this.logX = logX;
    }
    public String getYdatareference() {
        return yDataReference;
    }

    public void setYdatareference(String yDataReference) {
        this.yDataReference = yDataReference;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public sedml_listOfCurves getSedml_listofcurves() {
        return sedml_listofcurves;
    }

    public void setSedml_listofcurves(sedml_listOfCurves sedml_listofcurves) {
        this.sedml_listofcurves = sedml_listofcurves;
    }

}
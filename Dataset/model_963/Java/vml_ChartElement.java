





import java.util.List;
import java.util.ArrayList;

public class vml_ChartElement extends DiagramElement {

    private String yValue;
    private String ID;
    private String xValue;



    public vml_ChartElement(
        String yValue,        String ID,        String xValue    ) {
        super(
        );
        this.yValue = yValue;
        this.ID = ID;
        this.xValue = xValue;
    }


    public String getYvalue() {
        return yValue;
    }

    public void setYvalue(String yValue) {
        this.yValue = yValue;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getXvalue() {
        return xValue;
    }

    public void setXvalue(String xValue) {
        this.xValue = xValue;
    }


}
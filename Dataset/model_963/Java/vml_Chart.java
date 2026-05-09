





import java.util.List;
import java.util.ArrayList;

public class vml_Chart extends Diagram {

    private String xTitle;
    private String ID;
    private String title;
    private String yTitle;





    private vml_ChartWithAxisStyle vml_chartwithaxisstyle;


    public vml_Chart(
        String xTitle,        String ID,        String title,        String yTitle    ) {
        super(
        );
        this.xTitle = xTitle;
        this.ID = ID;
        this.title = title;
        this.yTitle = yTitle;
    }


    public String getXtitle() {
        return xTitle;
    }

    public void setXtitle(String xTitle) {
        this.xTitle = xTitle;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getYtitle() {
        return yTitle;
    }

    public void setYtitle(String yTitle) {
        this.yTitle = yTitle;
    }

    public vml_ChartWithAxisStyle getVml_chartwithaxisstyle() {
        return vml_chartwithaxisstyle;
    }

    public void setVml_chartwithaxisstyle(vml_ChartWithAxisStyle vml_chartwithaxisstyle) {
        this.vml_chartwithaxisstyle = vml_chartwithaxisstyle;
    }

}
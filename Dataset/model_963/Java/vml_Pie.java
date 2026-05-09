





import java.util.List;
import java.util.ArrayList;

public class vml_Pie extends Diagram {

    private String title;
    private String identifier;





    private vml_ChartWithoutAxisStyle vml_chartwithoutaxisstyle;


    public vml_Pie(
        String title,        String identifier    ) {
        super(
        );
        this.title = title;
        this.identifier = identifier;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public vml_ChartWithoutAxisStyle getVml_chartwithoutaxisstyle() {
        return vml_chartwithoutaxisstyle;
    }

    public void setVml_chartwithoutaxisstyle(vml_ChartWithoutAxisStyle vml_chartwithoutaxisstyle) {
        this.vml_chartwithoutaxisstyle = vml_chartwithoutaxisstyle;
    }

}
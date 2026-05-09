





import java.util.List;
import java.util.ArrayList;

public class eTJ_Title extends ColumnAttribute, ReportAttribute, NikuReportAttribute {

    private String title;



    public eTJ_Title(
        String title    ) {
        super(
        );
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}
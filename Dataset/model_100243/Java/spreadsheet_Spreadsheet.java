





import java.util.List;
import java.util.ArrayList;

public class spreadsheet_Spreadsheet  {

    private String Label;
    private String FilePath;



    public spreadsheet_Spreadsheet(
        String Label,        String FilePath    ) {
        this.Label = Label;
        this.FilePath = FilePath;
    }


    public String getLabel() {
        return Label;
    }

    public void setLabel(String Label) {
        this.Label = Label;
    }
    public String getFilepath() {
        return FilePath;
    }

    public void setFilepath(String FilePath) {
        this.FilePath = FilePath;
    }


}






import java.util.List;
import java.util.ArrayList;

public class spreadsheet_Spreadsheet  {

    private String Label;
    private String FilePath;





    private spreadsheet_Sheet spreadsheet_sheet;




    private List<spreadsheet_Sheet> spreadsheet_sheets;


    public spreadsheet_Spreadsheet(
        String Label,        String FilePath    ) {
        this.Label = Label;
        this.FilePath = FilePath;
        this.spreadsheet_sheets = new ArrayList<>();
    }

    public spreadsheet_Spreadsheet(
        String Label,        String FilePath        ArrayList<spreadsheet_Sheet> spreadsheet_sheets    ) {
        this.Label = Label;
        this.FilePath = FilePath;
        this.spreadsheet_sheets = spreadsheet_sheets;
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

    public spreadsheet_Sheet getSpreadsheet_sheet() {
        return spreadsheet_sheet;
    }

    public void setSpreadsheet_sheet(spreadsheet_Sheet spreadsheet_sheet) {
        this.spreadsheet_sheet = spreadsheet_sheet;
    }
    public List<spreadsheet_Sheet> getSpreadsheet_sheets() {
        return spreadsheet_sheets;
    }

    public void addSpreadsheet_sheet(Spreadsheet_sheet spreadsheet_sheet) {
        this.spreadsheet_sheets.add(spreadsheet_sheet);
    }

}
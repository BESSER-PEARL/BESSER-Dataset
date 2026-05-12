





import java.util.List;
import java.util.ArrayList;

public class spreadsheet_Text  {

    private String textContent;





    private spreadsheet_Sheet spreadsheet_sheet;


    public spreadsheet_Text(
        String textContent    ) {
        this.textContent = textContent;
    }


    public String getTextcontent() {
        return textContent;
    }

    public void setTextcontent(String textContent) {
        this.textContent = textContent;
    }

    public spreadsheet_Sheet getSpreadsheet_sheet() {
        return spreadsheet_sheet;
    }

    public void setSpreadsheet_sheet(spreadsheet_Sheet spreadsheet_sheet) {
        this.spreadsheet_sheet = spreadsheet_sheet;
    }

}
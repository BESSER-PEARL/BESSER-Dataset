





import java.util.List;
import java.util.ArrayList;

public class spreadsheet_Sheet  {

    private String name;





    private List<spreadsheet_Table> spreadsheet_tables;




    private List<spreadsheet_Image> spreadsheet_images;




    private spreadsheet_SpreadsheetFile spreadsheet_spreadsheetfile;


    public spreadsheet_Sheet(
        String name    ) {
        this.name = name;
        this.spreadsheet_tables = new ArrayList<>();
        this.spreadsheet_images = new ArrayList<>();
    }

    public spreadsheet_Sheet(
        String name        ArrayList<spreadsheet_Table> spreadsheet_tables,        ArrayList<spreadsheet_Image> spreadsheet_images    ) {
        this.name = name;
        this.spreadsheet_tables = spreadsheet_tables;
        this.spreadsheet_images = spreadsheet_images;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<spreadsheet_Table> getSpreadsheet_tables() {
        return spreadsheet_tables;
    }

    public void addSpreadsheet_table(Spreadsheet_table spreadsheet_table) {
        this.spreadsheet_tables.add(spreadsheet_table);
    }
    public List<spreadsheet_Image> getSpreadsheet_images() {
        return spreadsheet_images;
    }

    public void addSpreadsheet_image(Spreadsheet_image spreadsheet_image) {
        this.spreadsheet_images.add(spreadsheet_image);
    }
    public spreadsheet_SpreadsheetFile getSpreadsheet_spreadsheetfile() {
        return spreadsheet_spreadsheetfile;
    }

    public void setSpreadsheet_spreadsheetfile(spreadsheet_SpreadsheetFile spreadsheet_spreadsheetfile) {
        this.spreadsheet_spreadsheetfile = spreadsheet_spreadsheetfile;
    }

}
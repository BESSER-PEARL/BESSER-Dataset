





import java.util.List;
import java.util.ArrayList;

public class spreadsheet_Title extends ContentElement {

    private String hiearchy;





    private spreadsheet_Text spreadsheet_text;




    private spreadsheet_Table spreadsheet_table;




    private spreadsheet_Image spreadsheet_image;


    public spreadsheet_Title(
        String hiearchy    ) {
        super(
        );
        this.hiearchy = hiearchy;
    }


    public String getHiearchy() {
        return hiearchy;
    }

    public void setHiearchy(String hiearchy) {
        this.hiearchy = hiearchy;
    }

    public spreadsheet_Text getSpreadsheet_text() {
        return spreadsheet_text;
    }

    public void setSpreadsheet_text(spreadsheet_Text spreadsheet_text) {
        this.spreadsheet_text = spreadsheet_text;
    }
    public spreadsheet_Table getSpreadsheet_table() {
        return spreadsheet_table;
    }

    public void setSpreadsheet_table(spreadsheet_Table spreadsheet_table) {
        this.spreadsheet_table = spreadsheet_table;
    }
    public spreadsheet_Image getSpreadsheet_image() {
        return spreadsheet_image;
    }

    public void setSpreadsheet_image(spreadsheet_Image spreadsheet_image) {
        this.spreadsheet_image = spreadsheet_image;
    }

}
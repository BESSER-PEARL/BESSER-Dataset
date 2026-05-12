





import java.util.List;
import java.util.ArrayList;

public class spreadsheet_Point  {

    private int y;
    private int x;





    private spreadsheet_Cell spreadsheet_cell;




    private spreadsheet_Table spreadsheet_table;




    private spreadsheet_Image spreadsheet_image;


    public spreadsheet_Point(
        int y,        int x    ) {
        this.y = y;
        this.x = x;
    }


    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public spreadsheet_Cell getSpreadsheet_cell() {
        return spreadsheet_cell;
    }

    public void setSpreadsheet_cell(spreadsheet_Cell spreadsheet_cell) {
        this.spreadsheet_cell = spreadsheet_cell;
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
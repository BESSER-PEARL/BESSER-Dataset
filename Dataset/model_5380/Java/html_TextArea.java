





import java.util.List;
import java.util.ArrayList;

public class html_TextArea extends Editable {

    private int maxLength;
    private int rows;



    public html_TextArea(
        int maxLength,        int rows    ) {
        super(
        );
        this.maxLength = maxLength;
        this.rows = rows;
    }


    public int getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(int maxLength) {
        this.maxLength = maxLength;
    }
    public int getRows() {
        return rows;
    }

    public void setRows(int rows) {
        this.rows = rows;
    }


}
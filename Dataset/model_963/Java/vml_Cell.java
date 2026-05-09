





import java.util.List;
import java.util.ArrayList;

public class vml_Cell  {

    private String textValue;





    private vml_Row vml_row;




    private vml_Column vml_column;


    public vml_Cell(
        String textValue    ) {
        this.textValue = textValue;
    }


    public String getTextvalue() {
        return textValue;
    }

    public void setTextvalue(String textValue) {
        this.textValue = textValue;
    }

    public vml_Row getVml_row() {
        return vml_row;
    }

    public void setVml_row(vml_Row vml_row) {
        this.vml_row = vml_row;
    }
    public vml_Column getVml_column() {
        return vml_column;
    }

    public void setVml_column(vml_Column vml_column) {
        this.vml_column = vml_column;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Cell extends TableElement {

    private String formula;





    private Row row;


    public Cell(
        String formula    ) {
        super(
            int,            index        );
        this.formula = formula;
    }


    public String getFormula() {
        return formula;
    }

    public void setFormula(String formula) {
        this.formula = formula;
    }

    public Row getRow() {
        return row;
    }

    public void setRow(Row row) {
        this.row = row;
    }

}
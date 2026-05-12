





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLSimplified_Cell extends TableElement {

    private String mergeDown;
    private String formula;
    private String hRef;
    private String arrayRange;
    private String mergeAcross;





    private Data data;




    private Row row;


    public SpreadsheetMLSimplified_Cell(
        String mergeDown,        String formula,        String hRef,        String arrayRange,        String mergeAcross    ) {
        super(
        );
        this.mergeDown = mergeDown;
        this.formula = formula;
        this.hRef = hRef;
        this.arrayRange = arrayRange;
        this.mergeAcross = mergeAcross;
    }


    public String getMergedown() {
        return mergeDown;
    }

    public void setMergedown(String mergeDown) {
        this.mergeDown = mergeDown;
    }
    public String getFormula() {
        return formula;
    }

    public void setFormula(String formula) {
        this.formula = formula;
    }
    public String getHref() {
        return hRef;
    }

    public void setHref(String hRef) {
        this.hRef = hRef;
    }
    public String getArrayrange() {
        return arrayRange;
    }

    public void setArrayrange(String arrayRange) {
        this.arrayRange = arrayRange;
    }
    public String getMergeacross() {
        return mergeAcross;
    }

    public void setMergeacross(String mergeAcross) {
        this.mergeAcross = mergeAcross;
    }

    public Data getData() {
        return data;
    }

    public void setData(Data data) {
        this.data = data;
    }
    public Row getRow() {
        return row;
    }

    public void setRow(Row row) {
        this.row = row;
    }

}
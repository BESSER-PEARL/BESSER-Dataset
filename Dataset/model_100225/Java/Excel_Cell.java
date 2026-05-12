





import java.util.List;
import java.util.ArrayList;

public class Excel_Cell extends TableElement {

    private String arrayRange;
    private String hRef;
    private String formula;
    private String mergeAcross;
    private String mergeDown;





    private Data data;




    private Row row;


    public Excel_Cell(
        String arrayRange,        String hRef,        String formula,        String mergeAcross,        String mergeDown    ) {
        super(
        );
        this.arrayRange = arrayRange;
        this.hRef = hRef;
        this.formula = formula;
        this.mergeAcross = mergeAcross;
        this.mergeDown = mergeDown;
    }


    public String getArrayrange() {
        return arrayRange;
    }

    public void setArrayrange(String arrayRange) {
        this.arrayRange = arrayRange;
    }
    public String getHref() {
        return hRef;
    }

    public void setHref(String hRef) {
        this.hRef = hRef;
    }
    public String getFormula() {
        return formula;
    }

    public void setFormula(String formula) {
        this.formula = formula;
    }
    public String getMergeacross() {
        return mergeAcross;
    }

    public void setMergeacross(String mergeAcross) {
        this.mergeAcross = mergeAcross;
    }
    public String getMergedown() {
        return mergeDown;
    }

    public void setMergedown(String mergeDown) {
        this.mergeDown = mergeDown;
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
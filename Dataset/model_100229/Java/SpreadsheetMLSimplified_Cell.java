





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLSimplified_Cell extends TableElement {

    private String arrayRange;
    private String mergeAcross;
    private String hRef;
    private String formula;
    private String mergeDown;





    private Data data;


    public SpreadsheetMLSimplified_Cell(
        String arrayRange,        String mergeAcross,        String hRef,        String formula,        String mergeDown    ) {
        super(
        );
        this.arrayRange = arrayRange;
        this.mergeAcross = mergeAcross;
        this.hRef = hRef;
        this.formula = formula;
        this.mergeDown = mergeDown;
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

}






import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLSimplified_Cell extends TableElement {

    private float mergeDown;
    private float mergeAcross;
    private String arrayRange;
    private String formula;
    private String hRef;





    private SpreadsheetMLSimplified_Row spreadsheetmlsimplified_row;




    private SpreadsheetMLSimplified_Row spreadsheetmlsimplified_row;




    private SpreadsheetMLSimplified_Data spreadsheetmlsimplified_data;




    private SpreadsheetMLSimplified_Data spreadsheetmlsimplified_data;


    public SpreadsheetMLSimplified_Cell(
        float mergeDown,        float mergeAcross,        String arrayRange,        String formula,        String hRef    ) {
        super(
        );
        this.mergeDown = mergeDown;
        this.mergeAcross = mergeAcross;
        this.arrayRange = arrayRange;
        this.formula = formula;
        this.hRef = hRef;
    }


    public float getMergedown() {
        return mergeDown;
    }

    public void setMergedown(float mergeDown) {
        this.mergeDown = mergeDown;
    }
    public float getMergeacross() {
        return mergeAcross;
    }

    public void setMergeacross(float mergeAcross) {
        this.mergeAcross = mergeAcross;
    }
    public String getArrayrange() {
        return arrayRange;
    }

    public void setArrayrange(String arrayRange) {
        this.arrayRange = arrayRange;
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

    public SpreadsheetMLSimplified_Row getSpreadsheetmlsimplified_row() {
        return spreadsheetmlsimplified_row;
    }

    public void setSpreadsheetmlsimplified_row(SpreadsheetMLSimplified_Row spreadsheetmlsimplified_row) {
        this.spreadsheetmlsimplified_row = spreadsheetmlsimplified_row;
    }
    public SpreadsheetMLSimplified_Row getSpreadsheetmlsimplified_row() {
        return spreadsheetmlsimplified_row;
    }

    public void setSpreadsheetmlsimplified_row(SpreadsheetMLSimplified_Row spreadsheetmlsimplified_row) {
        this.spreadsheetmlsimplified_row = spreadsheetmlsimplified_row;
    }
    public SpreadsheetMLSimplified_Data getSpreadsheetmlsimplified_data() {
        return spreadsheetmlsimplified_data;
    }

    public void setSpreadsheetmlsimplified_data(SpreadsheetMLSimplified_Data spreadsheetmlsimplified_data) {
        this.spreadsheetmlsimplified_data = spreadsheetmlsimplified_data;
    }
    public SpreadsheetMLSimplified_Data getSpreadsheetmlsimplified_data() {
        return spreadsheetmlsimplified_data;
    }

    public void setSpreadsheetmlsimplified_data(SpreadsheetMLSimplified_Data spreadsheetmlsimplified_data) {
        this.spreadsheetmlsimplified_data = spreadsheetmlsimplified_data;
    }

}
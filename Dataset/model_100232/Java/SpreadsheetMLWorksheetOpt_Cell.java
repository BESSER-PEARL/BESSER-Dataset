





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLWorksheetOpt_Cell extends TableElement {

    private String arrayRange;
    private String formula;
    private String hRef;
    private String mergeDown;
    private String mergeAcross;





    private List<SmartTagsCollection> smarttagscollections;




    private Row row;




    private Data data;


    public SpreadsheetMLWorksheetOpt_Cell(
        String arrayRange,        String formula,        String hRef,        String mergeDown,        String mergeAcross    ) {
        super(
        );
        this.arrayRange = arrayRange;
        this.formula = formula;
        this.hRef = hRef;
        this.mergeDown = mergeDown;
        this.mergeAcross = mergeAcross;
        this.smarttagscollections = new ArrayList<>();
    }

    public SpreadsheetMLWorksheetOpt_Cell(
        String arrayRange,        String formula,        String hRef,        String mergeDown,        String mergeAcross        ArrayList<SmartTagsCollection> smarttagscollections    ) {
        this.arrayRange = arrayRange;
        this.formula = formula;
        this.hRef = hRef;
        this.mergeDown = mergeDown;
        this.mergeAcross = mergeAcross;
        this.smarttagscollections = smarttagscollections;
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
    public String getMergedown() {
        return mergeDown;
    }

    public void setMergedown(String mergeDown) {
        this.mergeDown = mergeDown;
    }
    public String getMergeacross() {
        return mergeAcross;
    }

    public void setMergeacross(String mergeAcross) {
        this.mergeAcross = mergeAcross;
    }

    public List<SmartTagsCollection> getSmarttagscollections() {
        return smarttagscollections;
    }

    public void addSmarttagscollection(Smarttagscollection smarttagscollection) {
        this.smarttagscollections.add(smarttagscollection);
    }
    public Row getRow() {
        return row;
    }

    public void setRow(Row row) {
        this.row = row;
    }
    public Data getData() {
        return data;
    }

    public void setData(Data data) {
        this.data = data;
    }

}
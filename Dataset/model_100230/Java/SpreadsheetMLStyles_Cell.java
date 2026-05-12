





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_Cell extends TableElement {

    private String mergeDown;
    private String arrayRange;
    private String formula;
    private String mergeAcross;
    private String hRef;





    private Row row;




    private List<SmartTagsCollection> smarttagscollections;




    private Data data;


    public SpreadsheetMLStyles_Cell(
        String mergeDown,        String arrayRange,        String formula,        String mergeAcross,        String hRef    ) {
        super(
        );
        this.mergeDown = mergeDown;
        this.arrayRange = arrayRange;
        this.formula = formula;
        this.mergeAcross = mergeAcross;
        this.hRef = hRef;
        this.smarttagscollections = new ArrayList<>();
    }

    public SpreadsheetMLStyles_Cell(
        String mergeDown,        String arrayRange,        String formula,        String mergeAcross,        String hRef        ArrayList<SmartTagsCollection> smarttagscollections    ) {
        this.mergeDown = mergeDown;
        this.arrayRange = arrayRange;
        this.formula = formula;
        this.mergeAcross = mergeAcross;
        this.hRef = hRef;
        this.smarttagscollections = smarttagscollections;
    }

    public String getMergedown() {
        return mergeDown;
    }

    public void setMergedown(String mergeDown) {
        this.mergeDown = mergeDown;
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

    public Row getRow() {
        return row;
    }

    public void setRow(Row row) {
        this.row = row;
    }
    public List<SmartTagsCollection> getSmarttagscollections() {
        return smarttagscollections;
    }

    public void addSmarttagscollection(Smarttagscollection smarttagscollection) {
        this.smarttagscollections.add(smarttagscollection);
    }
    public Data getData() {
        return data;
    }

    public void setData(Data data) {
        this.data = data;
    }

}
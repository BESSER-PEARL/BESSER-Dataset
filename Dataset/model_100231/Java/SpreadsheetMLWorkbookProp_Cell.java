





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLWorkbookProp_Cell extends TableElement {

    private String arrayRange;
    private String formula;
    private String mergeAcross;
    private String mergeDown;
    private String hRef;





    private Row row;




    private List<SmartTagsCollection> smarttagscollections;




    private Data data;


    public SpreadsheetMLWorkbookProp_Cell(
        String arrayRange,        String formula,        String mergeAcross,        String mergeDown,        String hRef    ) {
        super(
        );
        this.arrayRange = arrayRange;
        this.formula = formula;
        this.mergeAcross = mergeAcross;
        this.mergeDown = mergeDown;
        this.hRef = hRef;
        this.smarttagscollections = new ArrayList<>();
    }

    public SpreadsheetMLWorkbookProp_Cell(
        String arrayRange,        String formula,        String mergeAcross,        String mergeDown,        String hRef        ArrayList<SmartTagsCollection> smarttagscollections    ) {
        this.arrayRange = arrayRange;
        this.formula = formula;
        this.mergeAcross = mergeAcross;
        this.mergeDown = mergeDown;
        this.hRef = hRef;
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
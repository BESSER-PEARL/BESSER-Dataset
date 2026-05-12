





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLBasicDef_Cell extends TableElement {

    private String hRef;
    private String formula;
    private String arrayRange;
    private String mergeAcross;
    private String mergeDown;





    private Data data;




    private Row row;




    private List<SmartTagsCollection> smarttagscollections;


    public SpreadsheetMLBasicDef_Cell(
        String hRef,        String formula,        String arrayRange,        String mergeAcross,        String mergeDown    ) {
        super(
        );
        this.hRef = hRef;
        this.formula = formula;
        this.arrayRange = arrayRange;
        this.mergeAcross = mergeAcross;
        this.mergeDown = mergeDown;
        this.smarttagscollections = new ArrayList<>();
    }

    public SpreadsheetMLBasicDef_Cell(
        String hRef,        String formula,        String arrayRange,        String mergeAcross,        String mergeDown        ArrayList<SmartTagsCollection> smarttagscollections    ) {
        this.hRef = hRef;
        this.formula = formula;
        this.arrayRange = arrayRange;
        this.mergeAcross = mergeAcross;
        this.mergeDown = mergeDown;
        this.smarttagscollections = smarttagscollections;
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
    public List<SmartTagsCollection> getSmarttagscollections() {
        return smarttagscollections;
    }

    public void addSmarttagscollection(Smarttagscollection smarttagscollection) {
        this.smarttagscollections.add(smarttagscollection);
    }

}
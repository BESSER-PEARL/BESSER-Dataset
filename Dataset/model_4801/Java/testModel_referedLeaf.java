





import java.util.List;
import java.util.ArrayList;

public class testModel_referedLeaf extends Leafs {

    private int int;
    private String long;
    private String notChangeable;
    private String Float;
    private String name;
    private String ShortObj;
    private String short;
    private String Integer;
    private String LongObj;





    private testModel_ContainedLeaf testmodel_containedleaf;


    public testModel_referedLeaf(
        int int,        String long,        String notChangeable,        String Float,        String name,        String ShortObj,        String short,        String Integer,        String LongObj    ) {
        super(
        );
        this.int = int;
        this.long = long;
        this.notChangeable = notChangeable;
        this.Float = Float;
        this.name = name;
        this.ShortObj = ShortObj;
        this.short = short;
        this.Integer = Integer;
        this.LongObj = LongObj;
    }


    public int getInt() {
        return int;
    }

    public void setInt(int int) {
        this.int = int;
    }
    public String getLong() {
        return long;
    }

    public void setLong(String long) {
        this.long = long;
    }
    public String getNotchangeable() {
        return notChangeable;
    }

    public void setNotchangeable(String notChangeable) {
        this.notChangeable = notChangeable;
    }
    public String getFloat() {
        return Float;
    }

    public void setFloat(String Float) {
        this.Float = Float;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getShortobj() {
        return ShortObj;
    }

    public void setShortobj(String ShortObj) {
        this.ShortObj = ShortObj;
    }
    public String getShort() {
        return short;
    }

    public void setShort(String short) {
        this.short = short;
    }
    public String getInteger() {
        return Integer;
    }

    public void setInteger(String Integer) {
        this.Integer = Integer;
    }
    public String getLongobj() {
        return LongObj;
    }

    public void setLongobj(String LongObj) {
        this.LongObj = LongObj;
    }

    public testModel_ContainedLeaf getTestmodel_containedleaf() {
        return testmodel_containedleaf;
    }

    public void setTestmodel_containedleaf(testModel_ContainedLeaf testmodel_containedleaf) {
        this.testmodel_containedleaf = testmodel_containedleaf;
    }

}






import java.util.List;
import java.util.ArrayList;

public class testModel_referenziertesElement extends Element {

    private int int;
    private String name;
    private String LongObj;
    private String short;
    private String ShortObj;
    private String long;
    private String Integer;
    private String Float;
    private String notChangeable;





    private testModel_ContainedElement testmodel_containedelement;


    public testModel_referenziertesElement(
        int int,        String name,        String LongObj,        String short,        String ShortObj,        String long,        String Integer,        String Float,        String notChangeable    ) {
        super(
        );
        this.int = int;
        this.name = name;
        this.LongObj = LongObj;
        this.short = short;
        this.ShortObj = ShortObj;
        this.long = long;
        this.Integer = Integer;
        this.Float = Float;
        this.notChangeable = notChangeable;
    }


    public int getInt() {
        return int;
    }

    public void setInt(int int) {
        this.int = int;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLongobj() {
        return LongObj;
    }

    public void setLongobj(String LongObj) {
        this.LongObj = LongObj;
    }
    public String getShort() {
        return short;
    }

    public void setShort(String short) {
        this.short = short;
    }
    public String getShortobj() {
        return ShortObj;
    }

    public void setShortobj(String ShortObj) {
        this.ShortObj = ShortObj;
    }
    public String getLong() {
        return long;
    }

    public void setLong(String long) {
        this.long = long;
    }
    public String getInteger() {
        return Integer;
    }

    public void setInteger(String Integer) {
        this.Integer = Integer;
    }
    public String getFloat() {
        return Float;
    }

    public void setFloat(String Float) {
        this.Float = Float;
    }
    public String getNotchangeable() {
        return notChangeable;
    }

    public void setNotchangeable(String notChangeable) {
        this.notChangeable = notChangeable;
    }

    public testModel_ContainedElement getTestmodel_containedelement() {
        return testmodel_containedelement;
    }

    public void setTestmodel_containedelement(testModel_ContainedElement testmodel_containedelement) {
        this.testmodel_containedelement = testmodel_containedelement;
    }

}






import java.util.List;
import java.util.ArrayList;

public class testModel_Kategorie  {

    private String byte;
    private String bigint;
    private String Boolean;
    private boolean bool;
    private String name;
    private String bigdeci;





    private List<testModel_Kategorie> testmodel_kategories;


    public testModel_Kategorie(
        String byte,        String bigint,        String Boolean,        boolean bool,        String name,        String bigdeci    ) {
        this.byte = byte;
        this.bigint = bigint;
        this.Boolean = Boolean;
        this.bool = bool;
        this.name = name;
        this.bigdeci = bigdeci;
        this.testmodel_kategories = new ArrayList<>();
    }

    public testModel_Kategorie(
        String byte,        String bigint,        String Boolean,        boolean bool,        String name,        String bigdeci        ArrayList<testModel_Kategorie> testmodel_kategories    ) {
        this.byte = byte;
        this.bigint = bigint;
        this.Boolean = Boolean;
        this.bool = bool;
        this.name = name;
        this.bigdeci = bigdeci;
        this.testmodel_kategories = testmodel_kategories;
    }

    public String getByte() {
        return byte;
    }

    public void setByte(String byte) {
        this.byte = byte;
    }
    public String getBigint() {
        return bigint;
    }

    public void setBigint(String bigint) {
        this.bigint = bigint;
    }
    public String getBoolean() {
        return Boolean;
    }

    public void setBoolean(String Boolean) {
        this.Boolean = Boolean;
    }
    public boolean getBool() {
        return bool;
    }

    public void setBool(boolean bool) {
        this.bool = bool;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBigdeci() {
        return bigdeci;
    }

    public void setBigdeci(String bigdeci) {
        this.bigdeci = bigdeci;
    }

    public List<testModel_Kategorie> getTestmodel_kategories() {
        return testmodel_kategories;
    }

    public void addTestmodel_kategorie(Testmodel_kategorie testmodel_kategorie) {
        this.testmodel_kategories.add(testmodel_kategorie);
    }

}
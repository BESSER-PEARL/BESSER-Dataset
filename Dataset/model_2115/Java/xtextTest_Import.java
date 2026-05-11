





import java.util.List;
import java.util.ArrayList;

public class xtextTest_Import  {

    private String alias;
    private String id;





    private xtextTest_EmfTest xtexttest_emftest;


    public xtextTest_Import(
        String alias,        String id    ) {
        this.alias = alias;
        this.id = id;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public xtextTest_EmfTest getXtexttest_emftest() {
        return xtexttest_emftest;
    }

    public void setXtexttest_emftest(xtextTest_EmfTest xtexttest_emftest) {
        this.xtexttest_emftest = xtexttest_emftest;
    }

}
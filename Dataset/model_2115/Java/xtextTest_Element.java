





import java.util.List;
import java.util.ArrayList;

public class xtextTest_Element  {

    private String name;
    private String importing;





    private xtextTest_XtextTest xtexttest_xtexttest;




    private xtextTest_EmfTest xtexttest_emftest;


    public xtextTest_Element(
        String name,        String importing    ) {
        this.name = name;
        this.importing = importing;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getImporting() {
        return importing;
    }

    public void setImporting(String importing) {
        this.importing = importing;
    }

    public xtextTest_XtextTest getXtexttest_xtexttest() {
        return xtexttest_xtexttest;
    }

    public void setXtexttest_xtexttest(xtextTest_XtextTest xtexttest_xtexttest) {
        this.xtexttest_xtexttest = xtexttest_xtexttest;
    }
    public xtextTest_EmfTest getXtexttest_emftest() {
        return xtexttest_emftest;
    }

    public void setXtexttest_emftest(xtextTest_EmfTest xtexttest_emftest) {
        this.xtexttest_emftest = xtexttest_emftest;
    }

}






import java.util.List;
import java.util.ArrayList;

public class xtextTest_XtextTest  {

    private int timeOut;
    private String package;
    private String lang;
    private String imports;
    private String boolean;





    private xtextTest_Model xtexttest_model;


    public xtextTest_XtextTest(
        int timeOut,        String package,        String lang,        String imports,        String boolean    ) {
        this.timeOut = timeOut;
        this.package = package;
        this.lang = lang;
        this.imports = imports;
        this.boolean = boolean;
    }


    public int getTimeout() {
        return timeOut;
    }

    public void setTimeout(int timeOut) {
        this.timeOut = timeOut;
    }
    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getImports() {
        return imports;
    }

    public void setImports(String imports) {
        this.imports = imports;
    }
    public String getBoolean() {
        return boolean;
    }

    public void setBoolean(String boolean) {
        this.boolean = boolean;
    }

    public xtextTest_Model getXtexttest_model() {
        return xtexttest_model;
    }

    public void setXtexttest_model(xtextTest_Model xtexttest_model) {
        this.xtexttest_model = xtexttest_model;
    }

}
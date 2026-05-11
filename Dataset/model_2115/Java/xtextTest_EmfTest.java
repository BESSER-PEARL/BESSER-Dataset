





import java.util.List;
import java.util.ArrayList;

public class xtextTest_EmfTest  {

    private int timeOut;
    private String mydefault;
    private String file;
    private String package;





    private xtextTest_Model xtexttest_model;


    public xtextTest_EmfTest(
        int timeOut,        String mydefault,        String file,        String package    ) {
        this.timeOut = timeOut;
        this.mydefault = mydefault;
        this.file = file;
        this.package = package;
    }


    public int getTimeout() {
        return timeOut;
    }

    public void setTimeout(int timeOut) {
        this.timeOut = timeOut;
    }
    public String getMydefault() {
        return mydefault;
    }

    public void setMydefault(String mydefault) {
        this.mydefault = mydefault;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }

    public xtextTest_Model getXtexttest_model() {
        return xtexttest_model;
    }

    public void setXtexttest_model(xtextTest_Model xtexttest_model) {
        this.xtexttest_model = xtexttest_model;
    }

}
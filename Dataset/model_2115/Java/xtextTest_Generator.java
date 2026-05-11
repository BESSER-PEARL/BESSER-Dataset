





import java.util.List;
import java.util.ArrayList;

public class xtextTest_Generator  {

    private boolean isSameAsInputFile;
    private String output;
    private String patternFile;
    private String expected;
    private String exception;





    private xtextTest_XtextTest xtexttest_xtexttest;


    public xtextTest_Generator(
        boolean isSameAsInputFile,        String output,        String patternFile,        String expected,        String exception    ) {
        this.isSameAsInputFile = isSameAsInputFile;
        this.output = output;
        this.patternFile = patternFile;
        this.expected = expected;
        this.exception = exception;
    }


    public boolean getIssameasinputfile() {
        return isSameAsInputFile;
    }

    public void setIssameasinputfile(boolean isSameAsInputFile) {
        this.isSameAsInputFile = isSameAsInputFile;
    }
    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }
    public String getPatternfile() {
        return patternFile;
    }

    public void setPatternfile(String patternFile) {
        this.patternFile = patternFile;
    }
    public String getExpected() {
        return expected;
    }

    public void setExpected(String expected) {
        this.expected = expected;
    }
    public String getException() {
        return exception;
    }

    public void setException(String exception) {
        this.exception = exception;
    }

    public xtextTest_XtextTest getXtexttest_xtexttest() {
        return xtexttest_xtexttest;
    }

    public void setXtexttest_xtexttest(xtextTest_XtextTest xtexttest_xtexttest) {
        this.xtexttest_xtexttest = xtexttest_xtexttest;
    }

}
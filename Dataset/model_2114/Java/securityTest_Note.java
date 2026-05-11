





import java.util.List;
import java.util.ArrayList;

public class securityTest_Note  {

    private String noteText;





    private securityTest_Test securitytest_test;


    public securityTest_Note(
        String noteText    ) {
        this.noteText = noteText;
    }


    public String getNotetext() {
        return noteText;
    }

    public void setNotetext(String noteText) {
        this.noteText = noteText;
    }

    public securityTest_Test getSecuritytest_test() {
        return securitytest_test;
    }

    public void setSecuritytest_test(securityTest_Test securitytest_test) {
        this.securitytest_test = securitytest_test;
    }

}
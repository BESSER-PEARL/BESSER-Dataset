





import java.util.List;
import java.util.ArrayList;

public class adb_SubprogramDefault  {

    private String defaultName;





    private adb_FormalSubprogramDeclaration adb_formalsubprogramdeclaration;


    public adb_SubprogramDefault(
        String defaultName    ) {
        this.defaultName = defaultName;
    }


    public String getDefaultname() {
        return defaultName;
    }

    public void setDefaultname(String defaultName) {
        this.defaultName = defaultName;
    }

    public adb_FormalSubprogramDeclaration getAdb_formalsubprogramdeclaration() {
        return adb_formalsubprogramdeclaration;
    }

    public void setAdb_formalsubprogramdeclaration(adb_FormalSubprogramDeclaration adb_formalsubprogramdeclaration) {
        this.adb_formalsubprogramdeclaration = adb_formalsubprogramdeclaration;
    }

}






import java.util.List;
import java.util.ArrayList;

public class fsmtest_SignalDeclaration  {

    private String strVal;
    private String port;
    private String signame;
    private int intVal;



    public fsmtest_SignalDeclaration(
        String strVal,        String port,        String signame,        int intVal    ) {
        this.strVal = strVal;
        this.port = port;
        this.signame = signame;
        this.intVal = intVal;
    }


    public String getStrval() {
        return strVal;
    }

    public void setStrval(String strVal) {
        this.strVal = strVal;
    }
    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }
    public String getSigname() {
        return signame;
    }

    public void setSigname(String signame) {
        this.signame = signame;
    }
    public int getIntval() {
        return intVal;
    }

    public void setIntval(int intVal) {
        this.intVal = intVal;
    }


}
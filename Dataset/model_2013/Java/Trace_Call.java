





import java.util.List;
import java.util.ArrayList;

public class Trace_Call  {

    private String CPUTime;
    private String DBAccessesNumber;
    private String methodName;
    private String DBRowsNumber;





    private Level level;


    public Trace_Call(
        String CPUTime,        String DBAccessesNumber,        String methodName,        String DBRowsNumber    ) {
        this.CPUTime = CPUTime;
        this.DBAccessesNumber = DBAccessesNumber;
        this.methodName = methodName;
        this.DBRowsNumber = DBRowsNumber;
    }


    public String getCputime() {
        return CPUTime;
    }

    public void setCputime(String CPUTime) {
        this.CPUTime = CPUTime;
    }
    public String getDbaccessesnumber() {
        return DBAccessesNumber;
    }

    public void setDbaccessesnumber(String DBAccessesNumber) {
        this.DBAccessesNumber = DBAccessesNumber;
    }
    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }
    public String getDbrowsnumber() {
        return DBRowsNumber;
    }

    public void setDbrowsnumber(String DBRowsNumber) {
        this.DBRowsNumber = DBRowsNumber;
    }

    public Level getLevel() {
        return level;
    }

    public void setLevel(Level level) {
        this.level = level;
    }

}
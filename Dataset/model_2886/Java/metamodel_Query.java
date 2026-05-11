





import java.util.List;
import java.util.ArrayList;

public class metamodel_Query  {

    private String queryString;
    private String methodName;



    public metamodel_Query(
        String queryString,        String methodName    ) {
        this.queryString = queryString;
        this.methodName = methodName;
    }


    public String getQuerystring() {
        return queryString;
    }

    public void setQuerystring(String queryString) {
        this.queryString = queryString;
    }
    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }


}
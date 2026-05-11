





import java.util.List;
import java.util.ArrayList;

public class service_Selection extends FormalParameterList, NamedElement {

    private String methodName;
    private boolean distinct;
    private int limit;



    public service_Selection(
        String methodName,        boolean distinct,        int limit    ) {
        super(
        );
        this.methodName = methodName;
        this.distinct = distinct;
        this.limit = limit;
    }


    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }
    public boolean getDistinct() {
        return distinct;
    }

    public void setDistinct(boolean distinct) {
        this.distinct = distinct;
    }
    public int getLimit() {
        return limit;
    }

    public void setLimit(int limit) {
        this.limit = limit;
    }


}
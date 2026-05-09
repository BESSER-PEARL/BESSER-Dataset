





import java.util.List;
import java.util.ArrayList;

public class ocl_query_Query  {

    private String extentMap;





    private OCLExpression oclexpression;


    public ocl_query_Query(
        String extentMap    ) {
        this.extentMap = extentMap;
    }


    public String getExtentmap() {
        return extentMap;
    }

    public void setExtentmap(String extentMap) {
        this.extentMap = extentMap;
    }

    public OCLExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OCLExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}
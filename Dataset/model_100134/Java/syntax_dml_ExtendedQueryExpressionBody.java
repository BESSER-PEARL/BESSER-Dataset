





import java.util.List;
import java.util.ArrayList;

public class syntax_dml_ExtendedQueryExpressionBody extends QueryExpressionBody {

    private int optimizeRecordsNumber;



    public syntax_dml_ExtendedQueryExpressionBody(
        int optimizeRecordsNumber    ) {
        super(
        );
        this.optimizeRecordsNumber = optimizeRecordsNumber;
    }


    public int getOptimizerecordsnumber() {
        return optimizeRecordsNumber;
    }

    public void setOptimizerecordsnumber(int optimizeRecordsNumber) {
        this.optimizeRecordsNumber = optimizeRecordsNumber;
    }


}






import java.util.List;
import java.util.ArrayList;

public class analysis_profiler_BenchmarkReport extends AnalysisReport {

    private String column_names;



    public analysis_profiler_BenchmarkReport(
        String column_names    ) {
        super(
        );
        this.column_names = column_names;
    }


    public String getColumn_names() {
        return column_names;
    }

    public void setColumn_names(String column_names) {
        this.column_names = column_names;
    }


}
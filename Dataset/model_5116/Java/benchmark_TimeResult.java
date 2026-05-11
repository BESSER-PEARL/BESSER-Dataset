





import java.util.List;
import java.util.ArrayList;

public class benchmark_TimeResult  {

    private String elapsedMaxTime;
    private String elapsedTime;





    private benchmark_TestCase benchmark_testcase;




    private benchmark_Variant benchmark_variant;




    private benchmark_Variant benchmark_variant;


    public benchmark_TimeResult(
        String elapsedMaxTime,        String elapsedTime    ) {
        this.elapsedMaxTime = elapsedMaxTime;
        this.elapsedTime = elapsedTime;
    }


    public String getElapsedmaxtime() {
        return elapsedMaxTime;
    }

    public void setElapsedmaxtime(String elapsedMaxTime) {
        this.elapsedMaxTime = elapsedMaxTime;
    }
    public String getElapsedtime() {
        return elapsedTime;
    }

    public void setElapsedtime(String elapsedTime) {
        this.elapsedTime = elapsedTime;
    }

    public benchmark_TestCase getBenchmark_testcase() {
        return benchmark_testcase;
    }

    public void setBenchmark_testcase(benchmark_TestCase benchmark_testcase) {
        this.benchmark_testcase = benchmark_testcase;
    }
    public benchmark_Variant getBenchmark_variant() {
        return benchmark_variant;
    }

    public void setBenchmark_variant(benchmark_Variant benchmark_variant) {
        this.benchmark_variant = benchmark_variant;
    }
    public benchmark_Variant getBenchmark_variant() {
        return benchmark_variant;
    }

    public void setBenchmark_variant(benchmark_Variant benchmark_variant) {
        this.benchmark_variant = benchmark_variant;
    }

}
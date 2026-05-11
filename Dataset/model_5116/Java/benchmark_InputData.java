





import java.util.List;
import java.util.ArrayList;

public class benchmark_InputData extends NamedElement {






    private List<benchmark_TestCase> benchmark_testcases;




    private benchmark_TestCase benchmark_testcase;




    private benchmark_Scenario benchmark_scenario;


    public benchmark_InputData(
    ) {
        super(
        );
        this.benchmark_testcases = new ArrayList<>();
    }

    public benchmark_InputData(
        ArrayList<benchmark_TestCase> benchmark_testcases    ) {
        this.benchmark_testcases = benchmark_testcases;
    }


    public List<benchmark_TestCase> getBenchmark_testcases() {
        return benchmark_testcases;
    }

    public void addBenchmark_testcase(Benchmark_testcase benchmark_testcase) {
        this.benchmark_testcases.add(benchmark_testcase);
    }
    public benchmark_TestCase getBenchmark_testcase() {
        return benchmark_testcase;
    }

    public void setBenchmark_testcase(benchmark_TestCase benchmark_testcase) {
        this.benchmark_testcase = benchmark_testcase;
    }
    public benchmark_Scenario getBenchmark_scenario() {
        return benchmark_scenario;
    }

    public void setBenchmark_scenario(benchmark_Scenario benchmark_scenario) {
        this.benchmark_scenario = benchmark_scenario;
    }

}






import java.util.List;
import java.util.ArrayList;

public class benchmark_NamedElement  {

    private String name;





    private List<benchmark_Property> benchmark_propertys;


    public benchmark_NamedElement(
        String name    ) {
        this.name = name;
        this.benchmark_propertys = new ArrayList<>();
    }

    public benchmark_NamedElement(
        String name        ArrayList<benchmark_Property> benchmark_propertys    ) {
        this.name = name;
        this.benchmark_propertys = benchmark_propertys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<benchmark_Property> getBenchmark_propertys() {
        return benchmark_propertys;
    }

    public void addBenchmark_property(Benchmark_property benchmark_property) {
        this.benchmark_propertys.add(benchmark_property);
    }

}
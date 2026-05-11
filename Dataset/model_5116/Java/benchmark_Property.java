





import java.util.List;
import java.util.ArrayList;

public class benchmark_Property  {

    private String value;
    private String name;





    private benchmark_TimeResult benchmark_timeresult;


    public benchmark_Property(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public benchmark_TimeResult getBenchmark_timeresult() {
        return benchmark_timeresult;
    }

    public void setBenchmark_timeresult(benchmark_TimeResult benchmark_timeresult) {
        this.benchmark_timeresult = benchmark_timeresult;
    }

}
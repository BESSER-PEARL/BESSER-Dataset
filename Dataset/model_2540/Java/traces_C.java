





import java.util.List;
import java.util.ArrayList;

public class traces_C extends RootIn {

    private String name;





    private traces_A traces_a;


    public traces_C(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public traces_A getTraces_a() {
        return traces_a;
    }

    public void setTraces_a(traces_A traces_a) {
        this.traces_a = traces_a;
    }

}
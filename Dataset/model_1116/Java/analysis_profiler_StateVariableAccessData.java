





import java.util.List;
import java.util.ArrayList;

public class analysis_profiler_StateVariableAccessData extends MemoryAccessData {

    private String name;



    public analysis_profiler_StateVariableAccessData(
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


}
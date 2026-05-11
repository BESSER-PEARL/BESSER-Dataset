





import java.util.List;
import java.util.ArrayList;

public class trace_TraceElement  {

    private String name;
    private String runtimeObject;



    public trace_TraceElement(
        String name,        String runtimeObject    ) {
        this.name = name;
        this.runtimeObject = runtimeObject;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRuntimeobject() {
        return runtimeObject;
    }

    public void setRuntimeobject(String runtimeObject) {
        this.runtimeObject = runtimeObject;
    }


}
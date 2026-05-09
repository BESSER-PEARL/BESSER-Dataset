





import java.util.List;
import java.util.ArrayList;

public class trace_TraceElement  {

    private String runtimeObject;
    private String name;



    public trace_TraceElement(
        String runtimeObject,        String name    ) {
        this.runtimeObject = runtimeObject;
        this.name = name;
    }


    public String getRuntimeobject() {
        return runtimeObject;
    }

    public void setRuntimeobject(String runtimeObject) {
        this.runtimeObject = runtimeObject;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
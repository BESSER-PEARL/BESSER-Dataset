





import java.util.List;
import java.util.ArrayList;

public class trace_ModuleElement extends TraceElement {

    private String module_id;



    public trace_ModuleElement(
        String module_id    ) {
        super(
        );
        this.module_id = module_id;
    }


    public String getModule_id() {
        return module_id;
    }

    public void setModule_id(String module_id) {
        this.module_id = module_id;
    }


}
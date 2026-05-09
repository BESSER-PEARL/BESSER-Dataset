





import java.util.List;
import java.util.ArrayList;

public class uma_MethodLibrary extends MethodUnit {

    private String tool;





    private List<uma_MethodConfiguration> uma_methodconfigurations;


    public uma_MethodLibrary(
        String tool    ) {
        super(
        );
        this.tool = tool;
        this.uma_methodconfigurations = new ArrayList<>();
    }

    public uma_MethodLibrary(
        String tool        ArrayList<uma_MethodConfiguration> uma_methodconfigurations    ) {
        this.tool = tool;
        this.uma_methodconfigurations = uma_methodconfigurations;
    }

    public String getTool() {
        return tool;
    }

    public void setTool(String tool) {
        this.tool = tool;
    }

    public List<uma_MethodConfiguration> getUma_methodconfigurations() {
        return uma_methodconfigurations;
    }

    public void addUma_methodconfiguration(Uma_methodconfiguration uma_methodconfiguration) {
        this.uma_methodconfigurations.add(uma_methodconfiguration);
    }

}
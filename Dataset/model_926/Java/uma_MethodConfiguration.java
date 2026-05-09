





import java.util.List;
import java.util.ArrayList;

public class uma_MethodConfiguration extends MethodUnit {






    private uma_Process uma_process;




    private List<uma_MethodPackage> uma_methodpackages;




    private uma_MethodConfiguration uma_methodconfiguration;




    private uma_Process uma_process;


    public uma_MethodConfiguration(
    ) {
        super(
        );
        this.uma_methodpackages = new ArrayList<>();
    }

    public uma_MethodConfiguration(
        ArrayList<uma_MethodPackage> uma_methodpackages    ) {
        this.uma_methodpackages = uma_methodpackages;
    }


    public uma_Process getUma_process() {
        return uma_process;
    }

    public void setUma_process(uma_Process uma_process) {
        this.uma_process = uma_process;
    }
    public List<uma_MethodPackage> getUma_methodpackages() {
        return uma_methodpackages;
    }

    public void addUma_methodpackage(Uma_methodpackage uma_methodpackage) {
        this.uma_methodpackages.add(uma_methodpackage);
    }
    public uma_MethodConfiguration getUma_methodconfiguration() {
        return uma_methodconfiguration;
    }

    public void setUma_methodconfiguration(uma_MethodConfiguration uma_methodconfiguration) {
        this.uma_methodconfiguration = uma_methodconfiguration;
    }
    public uma_Process getUma_process() {
        return uma_process;
    }

    public void setUma_process(uma_Process uma_process) {
        this.uma_process = uma_process;
    }

}
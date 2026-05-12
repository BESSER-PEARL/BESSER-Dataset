





import java.util.List;
import java.util.ArrayList;

public class setup_EclipseIniTask extends SetupTask {

    private boolean vm;
    private String value;
    private String option;



    public setup_EclipseIniTask(
        boolean vm,        String value,        String option    ) {
        super(
        );
        this.vm = vm;
        this.value = value;
        this.option = option;
    }


    public boolean getVm() {
        return vm;
    }

    public void setVm(boolean vm) {
        this.vm = vm;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getOption() {
        return option;
    }

    public void setOption(String option) {
        this.option = option;
    }


}
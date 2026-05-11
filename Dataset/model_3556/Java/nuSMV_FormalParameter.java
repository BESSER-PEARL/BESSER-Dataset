





import java.util.List;
import java.util.ArrayList;

public class nuSMV_FormalParameter  {

    private String name;





    private nuSMV_Module nusmv_module;


    public nuSMV_FormalParameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public nuSMV_Module getNusmv_module() {
        return nusmv_module;
    }

    public void setNusmv_module(nuSMV_Module nusmv_module) {
        this.nusmv_module = nusmv_module;
    }

}
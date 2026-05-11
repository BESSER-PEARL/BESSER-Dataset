





import java.util.List;
import java.util.ArrayList;

public class nuSMV_Module  {

    private String name;





    private nuSMV_NuSmvModel nusmv_nusmvmodel;


    public nuSMV_Module(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public nuSMV_NuSmvModel getNusmv_nusmvmodel() {
        return nusmv_nusmvmodel;
    }

    public void setNusmv_nusmvmodel(nuSMV_NuSmvModel nusmv_nusmvmodel) {
        this.nusmv_nusmvmodel = nusmv_nusmvmodel;
    }

}
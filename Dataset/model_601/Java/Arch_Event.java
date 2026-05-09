





import java.util.List;
import java.util.ArrayList;

public class Arch_Event  {

    private String name;





    private Arch_Controller arch_controller;




    private Arch_GraphicControl arch_graphiccontrol;


    public Arch_Event(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Arch_Controller getArch_controller() {
        return arch_controller;
    }

    public void setArch_controller(Arch_Controller arch_controller) {
        this.arch_controller = arch_controller;
    }
    public Arch_GraphicControl getArch_graphiccontrol() {
        return arch_graphiccontrol;
    }

    public void setArch_graphiccontrol(Arch_GraphicControl arch_graphiccontrol) {
        this.arch_graphiccontrol = arch_graphiccontrol;
    }

}
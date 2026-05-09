





import java.util.List;
import java.util.ArrayList;

public class Arch_Div extends GraphicControl {






    private List<Arch_GraphicControl> arch_graphiccontrols;


    public Arch_Div(
    ) {
        super(
        );
        this.arch_graphiccontrols = new ArrayList<>();
    }

    public Arch_Div(
        ArrayList<Arch_GraphicControl> arch_graphiccontrols    ) {
        this.arch_graphiccontrols = arch_graphiccontrols;
    }


    public List<Arch_GraphicControl> getArch_graphiccontrols() {
        return arch_graphiccontrols;
    }

    public void addArch_graphiccontrol(Arch_graphiccontrol arch_graphiccontrol) {
        this.arch_graphiccontrols.add(arch_graphiccontrol);
    }

}
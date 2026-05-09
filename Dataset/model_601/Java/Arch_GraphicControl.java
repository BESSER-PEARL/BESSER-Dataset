





import java.util.List;
import java.util.ArrayList;

public class Arch_GraphicControl  {

    private String name;





    private Arch_View arch_view;


    public Arch_GraphicControl(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Arch_View getArch_view() {
        return arch_view;
    }

    public void setArch_view(Arch_View arch_view) {
        this.arch_view = arch_view;
    }

}
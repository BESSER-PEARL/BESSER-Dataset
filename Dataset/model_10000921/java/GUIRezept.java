





import java.util.List;
import java.util.ArrayList;

public class GUIRezept  {

    private String name;





    private GUI gui;




    private TeigRezept teigrezept;


    public GUIRezept(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public GUI getGui() {
        return gui;
    }

    public void setGui(GUI gui) {
        this.gui = gui;
    }
    public TeigRezept getTeigrezept() {
        return teigrezept;
    }

    public void setTeigrezept(TeigRezept teigrezept) {
        this.teigrezept = teigrezept;
    }

}
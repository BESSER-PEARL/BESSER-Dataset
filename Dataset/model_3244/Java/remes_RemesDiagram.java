





import java.util.List;
import java.util.ArrayList;

public class remes_RemesDiagram  {






    private List<remes_Mode> remes_modes;


    public remes_RemesDiagram(
    ) {
        this.remes_modes = new ArrayList<>();
    }

    public remes_RemesDiagram(
        ArrayList<remes_Mode> remes_modes    ) {
        this.remes_modes = remes_modes;
    }


    public List<remes_Mode> getRemes_modes() {
        return remes_modes;
    }

    public void addRemes_mode(Remes_mode remes_mode) {
        this.remes_modes.add(remes_mode);
    }

}
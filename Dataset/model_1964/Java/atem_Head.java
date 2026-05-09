





import java.util.List;
import java.util.ArrayList;

public class atem_Head  {






    private List<atem_HeadComponent> atem_headcomponents;




    private atem_AtemModel atem_atemmodel;


    public atem_Head(
    ) {
        this.atem_headcomponents = new ArrayList<>();
    }

    public atem_Head(
        ArrayList<atem_HeadComponent> atem_headcomponents    ) {
        this.atem_headcomponents = atem_headcomponents;
    }


    public List<atem_HeadComponent> getAtem_headcomponents() {
        return atem_headcomponents;
    }

    public void addAtem_headcomponent(Atem_headcomponent atem_headcomponent) {
        this.atem_headcomponents.add(atem_headcomponent);
    }
    public atem_AtemModel getAtem_atemmodel() {
        return atem_atemmodel;
    }

    public void setAtem_atemmodel(atem_AtemModel atem_atemmodel) {
        this.atem_atemmodel = atem_atemmodel;
    }

}
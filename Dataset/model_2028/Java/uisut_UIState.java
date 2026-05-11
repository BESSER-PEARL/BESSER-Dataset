





import java.util.List;
import java.util.ArrayList;

public class uisut_UIState extends AbstractState {

    private String pic;
    private boolean isInitial;





    private List<uisut_UIDataVariable> uisut_uidatavariables;




    private List<uisut_UIDataVariable> uisut_uidatavariables;




    private List<uisut_UIControl> uisut_uicontrols;


    public uisut_UIState(
        String pic,        boolean isInitial    ) {
        super(
        );
        this.pic = pic;
        this.isInitial = isInitial;
        this.uisut_uidatavariables = new ArrayList<>();
        this.uisut_uidatavariables = new ArrayList<>();
        this.uisut_uicontrols = new ArrayList<>();
    }

    public uisut_UIState(
        String pic,        boolean isInitial        ArrayList<uisut_UIDataVariable> uisut_uidatavariables,        ArrayList<uisut_UIDataVariable> uisut_uidatavariables,        ArrayList<uisut_UIControl> uisut_uicontrols    ) {
        this.pic = pic;
        this.isInitial = isInitial;
        this.uisut_uidatavariables = uisut_uidatavariables;
        this.uisut_uidatavariables = uisut_uidatavariables;
        this.uisut_uicontrols = uisut_uicontrols;
    }

    public String getPic() {
        return pic;
    }

    public void setPic(String pic) {
        this.pic = pic;
    }
    public boolean getIsinitial() {
        return isInitial;
    }

    public void setIsinitial(boolean isInitial) {
        this.isInitial = isInitial;
    }

    public List<uisut_UIDataVariable> getUisut_uidatavariables() {
        return uisut_uidatavariables;
    }

    public void addUisut_uidatavariable(Uisut_uidatavariable uisut_uidatavariable) {
        this.uisut_uidatavariables.add(uisut_uidatavariable);
    }
    public List<uisut_UIDataVariable> getUisut_uidatavariables() {
        return uisut_uidatavariables;
    }

    public void addUisut_uidatavariable(Uisut_uidatavariable uisut_uidatavariable) {
        this.uisut_uidatavariables.add(uisut_uidatavariable);
    }
    public List<uisut_UIControl> getUisut_uicontrols() {
        return uisut_uicontrols;
    }

    public void addUisut_uicontrol(Uisut_uicontrol uisut_uicontrol) {
        this.uisut_uicontrols.add(uisut_uicontrol);
    }

}
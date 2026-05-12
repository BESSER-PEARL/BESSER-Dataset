





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLBasicDef_MastersCollection  {






    private VisioDocument visiodocument;




    private List<MasterShortCut> mastershortcuts;




    private List<Master> masters;


    public DatadiagramMLBasicDef_MastersCollection(
    ) {
        this.mastershortcuts = new ArrayList<>();
        this.masters = new ArrayList<>();
    }

    public DatadiagramMLBasicDef_MastersCollection(
        ArrayList<MasterShortCut> mastershortcuts,        ArrayList<Master> masters    ) {
        this.mastershortcuts = mastershortcuts;
        this.masters = masters;
    }


    public VisioDocument getVisiodocument() {
        return visiodocument;
    }

    public void setVisiodocument(VisioDocument visiodocument) {
        this.visiodocument = visiodocument;
    }
    public List<MasterShortCut> getMastershortcuts() {
        return mastershortcuts;
    }

    public void addMastershortcut(Mastershortcut mastershortcut) {
        this.mastershortcuts.add(mastershortcut);
    }
    public List<Master> getMasters() {
        return masters;
    }

    public void addMaster(Master master) {
        this.masters.add(master);
    }

}






import java.util.List;
import java.util.ArrayList;

public class ccore_View  {

    private String icon;





    private List<ccore_ViewItemType> ccore_viewitemtypes;




    private ccore_ViewModel ccore_viewmodel;


    public ccore_View(
        String icon    ) {
        this.icon = icon;
        this.ccore_viewitemtypes = new ArrayList<>();
    }

    public ccore_View(
        String icon        ArrayList<ccore_ViewItemType> ccore_viewitemtypes    ) {
        this.icon = icon;
        this.ccore_viewitemtypes = ccore_viewitemtypes;
    }

    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }

    public List<ccore_ViewItemType> getCcore_viewitemtypes() {
        return ccore_viewitemtypes;
    }

    public void addCcore_viewitemtype(Ccore_viewitemtype ccore_viewitemtype) {
        this.ccore_viewitemtypes.add(ccore_viewitemtype);
    }
    public ccore_ViewModel getCcore_viewmodel() {
        return ccore_viewmodel;
    }

    public void setCcore_viewmodel(ccore_ViewModel ccore_viewmodel) {
        this.ccore_viewmodel = ccore_viewmodel;
    }

}
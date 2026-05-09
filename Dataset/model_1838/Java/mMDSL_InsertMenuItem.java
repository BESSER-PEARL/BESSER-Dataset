





import java.util.List;
import java.util.ArrayList;

public class mMDSL_InsertMenuItem  {

    private String menu;
    private String name;





    private mMDSL_MenuItem mmdsl_menuitem;


    public mMDSL_InsertMenuItem(
        String menu,        String name    ) {
        this.menu = menu;
        this.name = name;
    }


    public String getMenu() {
        return menu;
    }

    public void setMenu(String menu) {
        this.menu = menu;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mMDSL_MenuItem getMmdsl_menuitem() {
        return mmdsl_menuitem;
    }

    public void setMmdsl_menuitem(mMDSL_MenuItem mmdsl_menuitem) {
        this.mmdsl_menuitem = mmdsl_menuitem;
    }

}
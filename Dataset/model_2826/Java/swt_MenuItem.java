





import java.util.List;
import java.util.ArrayList;

public class swt_MenuItem extends Item {

    private int ID;
    private int accelerator;
    private String menuItemStyle;
    private boolean enabled;
    private boolean selection;





    private swt_AbstractMenu swt_abstractmenu;


    public swt_MenuItem(
        int ID,        int accelerator,        String menuItemStyle,        boolean enabled,        boolean selection    ) {
        super(
        );
        this.ID = ID;
        this.accelerator = accelerator;
        this.menuItemStyle = menuItemStyle;
        this.enabled = enabled;
        this.selection = selection;
    }


    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public int getAccelerator() {
        return accelerator;
    }

    public void setAccelerator(int accelerator) {
        this.accelerator = accelerator;
    }
    public String getMenuitemstyle() {
        return menuItemStyle;
    }

    public void setMenuitemstyle(String menuItemStyle) {
        this.menuItemStyle = menuItemStyle;
    }
    public boolean getEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }
    public boolean getSelection() {
        return selection;
    }

    public void setSelection(boolean selection) {
        this.selection = selection;
    }

    public swt_AbstractMenu getSwt_abstractmenu() {
        return swt_abstractmenu;
    }

    public void setSwt_abstractmenu(swt_AbstractMenu swt_abstractmenu) {
        this.swt_abstractmenu = swt_abstractmenu;
    }

}
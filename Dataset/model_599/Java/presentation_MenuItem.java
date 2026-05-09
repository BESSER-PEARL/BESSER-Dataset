





import java.util.List;
import java.util.ArrayList;

public class presentation_MenuItem extends Item {

    private String accelerator;
    private String group;
    private String selection;
    private String enabled;





    private presentation_Menu presentation_menu;




    private presentation_Menu presentation_menu;




    private presentation_Menu presentation_menu;




    private List<presentation_Menu> presentation_menus;




    private List<presentation_ICommand> presentation_icommands;




    private List<presentation_Menu> presentation_menus;


    public presentation_MenuItem(
        String accelerator,        String group,        String selection,        String enabled    ) {
        super(
        );
        this.accelerator = accelerator;
        this.group = group;
        this.selection = selection;
        this.enabled = enabled;
        this.presentation_menus = new ArrayList<>();
        this.presentation_icommands = new ArrayList<>();
        this.presentation_menus = new ArrayList<>();
    }

    public presentation_MenuItem(
        String accelerator,        String group,        String selection,        String enabled        ArrayList<presentation_Menu> presentation_menus,        ArrayList<presentation_ICommand> presentation_icommands,        ArrayList<presentation_Menu> presentation_menus    ) {
        this.accelerator = accelerator;
        this.group = group;
        this.selection = selection;
        this.enabled = enabled;
        this.presentation_menus = presentation_menus;
        this.presentation_icommands = presentation_icommands;
        this.presentation_menus = presentation_menus;
    }

    public String getAccelerator() {
        return accelerator;
    }

    public void setAccelerator(String accelerator) {
        this.accelerator = accelerator;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public String getEnabled() {
        return enabled;
    }

    public void setEnabled(String enabled) {
        this.enabled = enabled;
    }

    public presentation_Menu getPresentation_menu() {
        return presentation_menu;
    }

    public void setPresentation_menu(presentation_Menu presentation_menu) {
        this.presentation_menu = presentation_menu;
    }
    public presentation_Menu getPresentation_menu() {
        return presentation_menu;
    }

    public void setPresentation_menu(presentation_Menu presentation_menu) {
        this.presentation_menu = presentation_menu;
    }
    public presentation_Menu getPresentation_menu() {
        return presentation_menu;
    }

    public void setPresentation_menu(presentation_Menu presentation_menu) {
        this.presentation_menu = presentation_menu;
    }
    public List<presentation_Menu> getPresentation_menus() {
        return presentation_menus;
    }

    public void addPresentation_menu(Presentation_menu presentation_menu) {
        this.presentation_menus.add(presentation_menu);
    }
    public List<presentation_ICommand> getPresentation_icommands() {
        return presentation_icommands;
    }

    public void addPresentation_icommand(Presentation_icommand presentation_icommand) {
        this.presentation_icommands.add(presentation_icommand);
    }
    public List<presentation_Menu> getPresentation_menus() {
        return presentation_menus;
    }

    public void addPresentation_menu(Presentation_menu presentation_menu) {
        this.presentation_menus.add(presentation_menu);
    }

}
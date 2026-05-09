





import java.util.List;
import java.util.ArrayList;

public class presentation_Decorations extends Canvas {

    private String maximized;
    private String group4;
    private String minimized;
    private String images;
    private String image;
    private String text;





    private presentation_Menu presentation_menu;




    private List<presentation_Menu> presentation_menus;




    private List<presentation_Button> presentation_buttons;


    public presentation_Decorations(
        String maximized,        String group4,        String minimized,        String images,        String image,        String text    ) {
        super(
        );
        this.maximized = maximized;
        this.group4 = group4;
        this.minimized = minimized;
        this.images = images;
        this.image = image;
        this.text = text;
        this.presentation_menus = new ArrayList<>();
        this.presentation_buttons = new ArrayList<>();
    }

    public presentation_Decorations(
        String maximized,        String group4,        String minimized,        String images,        String image,        String text        ArrayList<presentation_Menu> presentation_menus,        ArrayList<presentation_Button> presentation_buttons    ) {
        this.maximized = maximized;
        this.group4 = group4;
        this.minimized = minimized;
        this.images = images;
        this.image = image;
        this.text = text;
        this.presentation_menus = presentation_menus;
        this.presentation_buttons = presentation_buttons;
    }

    public String getMaximized() {
        return maximized;
    }

    public void setMaximized(String maximized) {
        this.maximized = maximized;
    }
    public String getGroup4() {
        return group4;
    }

    public void setGroup4(String group4) {
        this.group4 = group4;
    }
    public String getMinimized() {
        return minimized;
    }

    public void setMinimized(String minimized) {
        this.minimized = minimized;
    }
    public String getImages() {
        return images;
    }

    public void setImages(String images) {
        this.images = images;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
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
    public List<presentation_Button> getPresentation_buttons() {
        return presentation_buttons;
    }

    public void addPresentation_button(Presentation_button presentation_button) {
        this.presentation_buttons.add(presentation_button);
    }

}
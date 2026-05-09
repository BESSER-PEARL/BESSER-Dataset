





import java.util.List;
import java.util.ArrayList;

public class presentation_Caret extends Widget {

    private String size;
    private String group;
    private String bounds;
    private String font;
    private String visible;
    private String location;
    private String image;





    private List<presentation_Canvas> presentation_canvass;




    private presentation_Canvas presentation_canvas;


    public presentation_Caret(
        String size,        String group,        String bounds,        String font,        String visible,        String location,        String image    ) {
        super(
        );
        this.size = size;
        this.group = group;
        this.bounds = bounds;
        this.font = font;
        this.visible = visible;
        this.location = location;
        this.image = image;
        this.presentation_canvass = new ArrayList<>();
    }

    public presentation_Caret(
        String size,        String group,        String bounds,        String font,        String visible,        String location,        String image        ArrayList<presentation_Canvas> presentation_canvass    ) {
        this.size = size;
        this.group = group;
        this.bounds = bounds;
        this.font = font;
        this.visible = visible;
        this.location = location;
        this.image = image;
        this.presentation_canvass = presentation_canvass;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getBounds() {
        return bounds;
    }

    public void setBounds(String bounds) {
        this.bounds = bounds;
    }
    public String getFont() {
        return font;
    }

    public void setFont(String font) {
        this.font = font;
    }
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public List<presentation_Canvas> getPresentation_canvass() {
        return presentation_canvass;
    }

    public void addPresentation_canvas(Presentation_canvas presentation_canvas) {
        this.presentation_canvass.add(presentation_canvas);
    }
    public presentation_Canvas getPresentation_canvas() {
        return presentation_canvas;
    }

    public void setPresentation_canvas(presentation_Canvas presentation_canvas) {
        this.presentation_canvas = presentation_canvas;
    }

}
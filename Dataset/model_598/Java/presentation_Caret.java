





import java.util.List;
import java.util.ArrayList;

public class presentation_Caret extends Widget {

    private String image;
    private String visible;
    private String bounds;
    private String size;
    private String font;
    private String group;
    private String location;





    private presentation_Canvas presentation_canvas;




    private List<presentation_Canvas> presentation_canvass;


    public presentation_Caret(
        String image,        String visible,        String bounds,        String size,        String font,        String group,        String location    ) {
        super(
        );
        this.image = image;
        this.visible = visible;
        this.bounds = bounds;
        this.size = size;
        this.font = font;
        this.group = group;
        this.location = location;
        this.presentation_canvass = new ArrayList<>();
    }

    public presentation_Caret(
        String image,        String visible,        String bounds,        String size,        String font,        String group,        String location        ArrayList<presentation_Canvas> presentation_canvass    ) {
        this.image = image;
        this.visible = visible;
        this.bounds = bounds;
        this.size = size;
        this.font = font;
        this.group = group;
        this.location = location;
        this.presentation_canvass = presentation_canvass;
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }
    public String getBounds() {
        return bounds;
    }

    public void setBounds(String bounds) {
        this.bounds = bounds;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getFont() {
        return font;
    }

    public void setFont(String font) {
        this.font = font;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public presentation_Canvas getPresentation_canvas() {
        return presentation_canvas;
    }

    public void setPresentation_canvas(presentation_Canvas presentation_canvas) {
        this.presentation_canvas = presentation_canvas;
    }
    public List<presentation_Canvas> getPresentation_canvass() {
        return presentation_canvass;
    }

    public void addPresentation_canvas(Presentation_canvas presentation_canvas) {
        this.presentation_canvass.add(presentation_canvas);
    }

}
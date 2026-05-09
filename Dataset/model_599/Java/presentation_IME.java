





import java.util.List;
import java.util.ArrayList;

public class presentation_IME extends Widget {

    private String text;
    private String compositionOffset;
    private String group;
    private String ranges;





    private presentation_Canvas presentation_canvas;


    public presentation_IME(
        String text,        String compositionOffset,        String group,        String ranges    ) {
        super(
        );
        this.text = text;
        this.compositionOffset = compositionOffset;
        this.group = group;
        this.ranges = ranges;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getCompositionoffset() {
        return compositionOffset;
    }

    public void setCompositionoffset(String compositionOffset) {
        this.compositionOffset = compositionOffset;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getRanges() {
        return ranges;
    }

    public void setRanges(String ranges) {
        this.ranges = ranges;
    }

    public presentation_Canvas getPresentation_canvas() {
        return presentation_canvas;
    }

    public void setPresentation_canvas(presentation_Canvas presentation_canvas) {
        this.presentation_canvas = presentation_canvas;
    }

}






import java.util.List;
import java.util.ArrayList;

public class presentation_IME extends Widget {

    private String ranges;
    private String group;
    private String compositionOffset;
    private String text;





    private presentation_Canvas presentation_canvas;


    public presentation_IME(
        String ranges,        String group,        String compositionOffset,        String text    ) {
        super(
        );
        this.ranges = ranges;
        this.group = group;
        this.compositionOffset = compositionOffset;
        this.text = text;
    }


    public String getRanges() {
        return ranges;
    }

    public void setRanges(String ranges) {
        this.ranges = ranges;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getCompositionoffset() {
        return compositionOffset;
    }

    public void setCompositionoffset(String compositionOffset) {
        this.compositionOffset = compositionOffset;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public presentation_Canvas getPresentation_canvas() {
        return presentation_canvas;
    }

    public void setPresentation_canvas(presentation_Canvas presentation_canvas) {
        this.presentation_canvas = presentation_canvas;
    }

}
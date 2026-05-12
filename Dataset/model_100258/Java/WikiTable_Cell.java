





import java.util.List;
import java.util.ArrayList;

public class WikiTable_Cell extends LocatedElement {

    private String isHeading;
    private String align;
    private String style;
    private String content;



    public WikiTable_Cell(
        String isHeading,        String align,        String style,        String content    ) {
        super(
        );
        this.isHeading = isHeading;
        this.align = align;
        this.style = style;
        this.content = content;
    }


    public String getIsheading() {
        return isHeading;
    }

    public void setIsheading(String isHeading) {
        this.isHeading = isHeading;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }


}
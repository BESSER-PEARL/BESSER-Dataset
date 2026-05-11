





import java.util.List;
import java.util.ArrayList;

public class HTML_TR extends HTMLElement {

    private String height;
    private String valign;
    private String align;
    private String bgcolor;





    private HTML_TABLE html_table;


    public HTML_TR(
        String height,        String valign,        String align,        String bgcolor    ) {
        super(
        );
        this.height = height;
        this.valign = valign;
        this.align = align;
        this.bgcolor = bgcolor;
    }


    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getBgcolor() {
        return bgcolor;
    }

    public void setBgcolor(String bgcolor) {
        this.bgcolor = bgcolor;
    }

    public HTML_TABLE getHtml_table() {
        return html_table;
    }

    public void setHtml_table(HTML_TABLE html_table) {
        this.html_table = html_table;
    }

}
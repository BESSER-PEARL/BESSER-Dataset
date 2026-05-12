





import java.util.List;
import java.util.ArrayList;

public class HTML_FRAMESET  {

    private String border;
    private String frameborder;
    private String framespacing;
    private String cols;
    private String rows;



    public HTML_FRAMESET(
        String border,        String frameborder,        String framespacing,        String cols,        String rows    ) {
        this.border = border;
        this.frameborder = frameborder;
        this.framespacing = framespacing;
        this.cols = cols;
        this.rows = rows;
    }


    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getFrameborder() {
        return frameborder;
    }

    public void setFrameborder(String frameborder) {
        this.frameborder = frameborder;
    }
    public String getFramespacing() {
        return framespacing;
    }

    public void setFramespacing(String framespacing) {
        this.framespacing = framespacing;
    }
    public String getCols() {
        return cols;
    }

    public void setCols(String cols) {
        this.cols = cols;
    }
    public String getRows() {
        return rows;
    }

    public void setRows(String rows) {
        this.rows = rows;
    }


}
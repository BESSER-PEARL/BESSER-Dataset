





import java.util.List;
import java.util.ArrayList;

public class HTML_FRAMESET  {

    private String border;
    private String framespacing;
    private String rows;
    private String cols;
    private String frameborder;



    public HTML_FRAMESET(
        String border,        String framespacing,        String rows,        String cols,        String frameborder    ) {
        this.border = border;
        this.framespacing = framespacing;
        this.rows = rows;
        this.cols = cols;
        this.frameborder = frameborder;
    }


    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getFramespacing() {
        return framespacing;
    }

    public void setFramespacing(String framespacing) {
        this.framespacing = framespacing;
    }
    public String getRows() {
        return rows;
    }

    public void setRows(String rows) {
        this.rows = rows;
    }
    public String getCols() {
        return cols;
    }

    public void setCols(String cols) {
        this.cols = cols;
    }
    public String getFrameborder() {
        return frameborder;
    }

    public void setFrameborder(String frameborder) {
        this.frameborder = frameborder;
    }


}
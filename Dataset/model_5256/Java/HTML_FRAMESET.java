





import java.util.List;
import java.util.ArrayList;

public class HTML_FRAMESET  {

    private String rows;
    private String framespacing;
    private String cols;
    private String frameborder;
    private String border;



    public HTML_FRAMESET(
        String rows,        String framespacing,        String cols,        String frameborder,        String border    ) {
        this.rows = rows;
        this.framespacing = framespacing;
        this.cols = cols;
        this.frameborder = frameborder;
        this.border = border;
    }


    public String getRows() {
        return rows;
    }

    public void setRows(String rows) {
        this.rows = rows;
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
    public String getFrameborder() {
        return frameborder;
    }

    public void setFrameborder(String frameborder) {
        this.frameborder = frameborder;
    }
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }


}
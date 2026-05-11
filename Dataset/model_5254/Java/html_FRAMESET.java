





import java.util.List;
import java.util.ArrayList;

public class html_FRAMESET  {

    private String framespacing;
    private String rows;
    private String border;
    private String frameborder;
    private String cols;



    public html_FRAMESET(
        String framespacing,        String rows,        String border,        String frameborder,        String cols    ) {
        this.framespacing = framespacing;
        this.rows = rows;
        this.border = border;
        this.frameborder = frameborder;
        this.cols = cols;
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
    public String getCols() {
        return cols;
    }

    public void setCols(String cols) {
        this.cols = cols;
    }


}
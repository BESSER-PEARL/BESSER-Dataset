





import java.util.List;
import java.util.ArrayList;

public class html_FRAMESET  {

    private String cols;
    private String rows;
    private String framespacing;
    private String frameborder;
    private String border;



    public html_FRAMESET(
        String cols,        String rows,        String framespacing,        String frameborder,        String border    ) {
        this.cols = cols;
        this.rows = rows;
        this.framespacing = framespacing;
        this.frameborder = frameborder;
        this.border = border;
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
    public String getFramespacing() {
        return framespacing;
    }

    public void setFramespacing(String framespacing) {
        this.framespacing = framespacing;
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
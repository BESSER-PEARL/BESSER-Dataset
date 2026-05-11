





import java.util.List;
import java.util.ArrayList;

public class html_FRAMESET  {

    private String border;
    private String rows;
    private String cols;
    private String frameborder;
    private String framespacing;



    public html_FRAMESET(
        String border,        String rows,        String cols,        String frameborder,        String framespacing    ) {
        this.border = border;
        this.rows = rows;
        this.cols = cols;
        this.frameborder = frameborder;
        this.framespacing = framespacing;
    }


    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
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
    public String getFramespacing() {
        return framespacing;
    }

    public void setFramespacing(String framespacing) {
        this.framespacing = framespacing;
    }


}
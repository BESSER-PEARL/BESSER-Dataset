





import java.util.List;
import java.util.ArrayList;

public class defaultname_FRAMESET  {

    private String frameborder;
    private String cols;
    private String border;
    private String rows;
    private String framespacing;



    public defaultname_FRAMESET(
        String frameborder,        String cols,        String border,        String rows,        String framespacing    ) {
        this.frameborder = frameborder;
        this.cols = cols;
        this.border = border;
        this.rows = rows;
        this.framespacing = framespacing;
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
    public String getFramespacing() {
        return framespacing;
    }

    public void setFramespacing(String framespacing) {
        this.framespacing = framespacing;
    }


}
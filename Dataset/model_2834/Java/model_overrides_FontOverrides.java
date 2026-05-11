





import java.util.List;
import java.util.ArrayList;

public class model_overrides_FontOverrides  {

    private String bold;
    private String size;
    private String underline;
    private String italic;



    public model_overrides_FontOverrides(
        String bold,        String size,        String underline,        String italic    ) {
        this.bold = bold;
        this.size = size;
        this.underline = underline;
        this.italic = italic;
    }


    public String getBold() {
        return bold;
    }

    public void setBold(String bold) {
        this.bold = bold;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getUnderline() {
        return underline;
    }

    public void setUnderline(String underline) {
        this.underline = underline;
    }
    public String getItalic() {
        return italic;
    }

    public void setItalic(String italic) {
        this.italic = italic;
    }


}
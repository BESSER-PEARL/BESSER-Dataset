





import java.util.List;
import java.util.ArrayList;

public class model_overrides_FontOverrides  {

    private String italic;
    private String size;
    private String bold;
    private String underline;



    public model_overrides_FontOverrides(
        String italic,        String size,        String bold,        String underline    ) {
        this.italic = italic;
        this.size = size;
        this.bold = bold;
        this.underline = underline;
    }


    public String getItalic() {
        return italic;
    }

    public void setItalic(String italic) {
        this.italic = italic;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getBold() {
        return bold;
    }

    public void setBold(String bold) {
        this.bold = bold;
    }
    public String getUnderline() {
        return underline;
    }

    public void setUnderline(String underline) {
        this.underline = underline;
    }


}
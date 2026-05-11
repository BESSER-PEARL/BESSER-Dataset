





import java.util.List;
import java.util.ArrayList;

public class model_Font  {

    private String italic;
    private String underline;
    private String bold;
    private String size;



    public model_Font(
        String italic,        String underline,        String bold,        String size    ) {
        this.italic = italic;
        this.underline = underline;
        this.bold = bold;
        this.size = size;
    }


    public String getItalic() {
        return italic;
    }

    public void setItalic(String italic) {
        this.italic = italic;
    }
    public String getUnderline() {
        return underline;
    }

    public void setUnderline(String underline) {
        this.underline = underline;
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


}
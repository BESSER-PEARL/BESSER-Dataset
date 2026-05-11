





import java.util.List;
import java.util.ArrayList;

public class model_Font  {

    private String bold;
    private String size;
    private String italic;
    private String underline;



    public model_Font(
        String bold,        String size,        String italic,        String underline    ) {
        this.bold = bold;
        this.size = size;
        this.italic = italic;
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


}
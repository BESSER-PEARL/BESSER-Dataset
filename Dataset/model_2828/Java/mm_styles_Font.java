





import java.util.List;
import java.util.ArrayList;

public class mm_styles_Font  {

    private boolean italic;
    private int size;
    private boolean bold;
    private String name;



    public mm_styles_Font(
        boolean italic,        int size,        boolean bold,        String name    ) {
        this.italic = italic;
        this.size = size;
        this.bold = bold;
        this.name = name;
    }


    public boolean getItalic() {
        return italic;
    }

    public void setItalic(boolean italic) {
        this.italic = italic;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public boolean getBold() {
        return bold;
    }

    public void setBold(boolean bold) {
        this.bold = bold;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
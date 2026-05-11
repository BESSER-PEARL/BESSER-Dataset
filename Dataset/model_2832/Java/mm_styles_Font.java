





import java.util.List;
import java.util.ArrayList;

public class mm_styles_Font  {

    private boolean bold;
    private boolean italic;
    private String name;
    private int size;



    public mm_styles_Font(
        boolean bold,        boolean italic,        String name,        int size    ) {
        this.bold = bold;
        this.italic = italic;
        this.name = name;
        this.size = size;
    }


    public boolean getBold() {
        return bold;
    }

    public void setBold(boolean bold) {
        this.bold = bold;
    }
    public boolean getItalic() {
        return italic;
    }

    public void setItalic(boolean italic) {
        this.italic = italic;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }


}
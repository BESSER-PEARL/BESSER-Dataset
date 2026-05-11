





import java.util.List;
import java.util.ArrayList;

public class mm_styles_Font  {

    private int size;
    private boolean italic;
    private String name;
    private boolean bold;



    public mm_styles_Font(
        int size,        boolean italic,        String name,        boolean bold    ) {
        this.size = size;
        this.italic = italic;
        this.name = name;
        this.bold = bold;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
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
    public boolean getBold() {
        return bold;
    }

    public void setBold(boolean bold) {
        this.bold = bold;
    }


}
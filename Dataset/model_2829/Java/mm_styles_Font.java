





import java.util.List;
import java.util.ArrayList;

public class mm_styles_Font  {

    private boolean italic;
    private int size;
    private String name;
    private boolean bold;



    public mm_styles_Font(
        boolean italic,        int size,        String name,        boolean bold    ) {
        this.italic = italic;
        this.size = size;
        this.name = name;
        this.bold = bold;
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






import java.util.List;
import java.util.ArrayList;

public class model_ScreenFont  {

    private String name;
    private boolean bold;
    private boolean italic;
    private String available;
    private String size;





    private model_Screen model_screen;


    public model_ScreenFont(
        String name,        boolean bold,        boolean italic,        String available,        String size    ) {
        this.name = name;
        this.bold = bold;
        this.italic = italic;
        this.available = available;
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
    public boolean getItalic() {
        return italic;
    }

    public void setItalic(boolean italic) {
        this.italic = italic;
    }
    public String getAvailable() {
        return available;
    }

    public void setAvailable(String available) {
        this.available = available;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public model_Screen getModel_screen() {
        return model_screen;
    }

    public void setModel_screen(model_Screen model_screen) {
        this.model_screen = model_screen;
    }

}






import java.util.List;
import java.util.ArrayList;

public class model_ScreenFont  {

    private String available;
    private boolean italic;
    private boolean bold;
    private String name;
    private String size;





    private model_Screen model_screen;


    public model_ScreenFont(
        String available,        boolean italic,        boolean bold,        String name,        String size    ) {
        this.available = available;
        this.italic = italic;
        this.bold = bold;
        this.name = name;
        this.size = size;
    }


    public String getAvailable() {
        return available;
    }

    public void setAvailable(String available) {
        this.available = available;
    }
    public boolean getItalic() {
        return italic;
    }

    public void setItalic(boolean italic) {
        this.italic = italic;
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






import java.util.List;
import java.util.ArrayList;

public class model_ScreenFont  {

    private boolean italic;
    private String size;
    private boolean bold;
    private String available;
    private String name;





    private model_Screen model_screen;


    public model_ScreenFont(
        boolean italic,        String size,        boolean bold,        String available,        String name    ) {
        this.italic = italic;
        this.size = size;
        this.bold = bold;
        this.available = available;
        this.name = name;
    }


    public boolean getItalic() {
        return italic;
    }

    public void setItalic(boolean italic) {
        this.italic = italic;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public boolean getBold() {
        return bold;
    }

    public void setBold(boolean bold) {
        this.bold = bold;
    }
    public String getAvailable() {
        return available;
    }

    public void setAvailable(String available) {
        this.available = available;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_Screen getModel_screen() {
        return model_screen;
    }

    public void setModel_screen(model_Screen model_screen) {
        this.model_screen = model_screen;
    }

}
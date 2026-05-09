





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Layer  {

    private int fill;
    private String name;
    private boolean visible;
    private boolean active;
    private int color;
    private int number;





    private eaglemodel_Layers eaglemodel_layers;


    public eaglemodel_Layer(
        int fill,        String name,        boolean visible,        boolean active,        int color,        int number    ) {
        this.fill = fill;
        this.name = name;
        this.visible = visible;
        this.active = active;
        this.color = color;
        this.number = number;
    }


    public int getFill() {
        return fill;
    }

    public void setFill(int fill) {
        this.fill = fill;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }
    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public int getColor() {
        return color;
    }

    public void setColor(int color) {
        this.color = color;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public eaglemodel_Layers getEaglemodel_layers() {
        return eaglemodel_layers;
    }

    public void setEaglemodel_layers(eaglemodel_Layers eaglemodel_layers) {
        this.eaglemodel_layers = eaglemodel_layers;
    }

}






import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Class  {

    private float drill;
    private float width;
    private int number;
    private String name;



    public eaglemodel_Class(
        float drill,        float width,        int number,        String name    ) {
        this.drill = drill;
        this.width = width;
        this.number = number;
        this.name = name;
    }


    public float getDrill() {
        return drill;
    }

    public void setDrill(float drill) {
        this.drill = drill;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
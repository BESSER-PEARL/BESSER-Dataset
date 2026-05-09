





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Pin  {

    private int rot;
    private float y;
    private String name;
    private String direction;
    private int swaplevel;
    private float x;
    private String length;
    private String function;
    private String visible;



    public eaglemodel_Pin(
        int rot,        float y,        String name,        String direction,        int swaplevel,        float x,        String length,        String function,        String visible    ) {
        this.rot = rot;
        this.y = y;
        this.name = name;
        this.direction = direction;
        this.swaplevel = swaplevel;
        this.x = x;
        this.length = length;
        this.function = function;
        this.visible = visible;
    }


    public int getRot() {
        return rot;
    }

    public void setRot(int rot) {
        this.rot = rot;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public int getSwaplevel() {
        return swaplevel;
    }

    public void setSwaplevel(int swaplevel) {
        this.swaplevel = swaplevel;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }
    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }


}
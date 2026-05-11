





import java.util.List;
import java.util.ArrayList;

public class minilang_Program  {

    private float x;
    private String angle;
    private float distance;
    private float y;





    private List<minilang_Line> minilang_lines;


    public minilang_Program(
        float x,        String angle,        float distance,        float y    ) {
        this.x = x;
        this.angle = angle;
        this.distance = distance;
        this.y = y;
        this.minilang_lines = new ArrayList<>();
    }

    public minilang_Program(
        float x,        String angle,        float distance,        float y        ArrayList<minilang_Line> minilang_lines    ) {
        this.x = x;
        this.angle = angle;
        this.distance = distance;
        this.y = y;
        this.minilang_lines = minilang_lines;
    }

    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }
    public float getDistance() {
        return distance;
    }

    public void setDistance(float distance) {
        this.distance = distance;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }

    public List<minilang_Line> getMinilang_lines() {
        return minilang_lines;
    }

    public void addMinilang_line(Minilang_line minilang_line) {
        this.minilang_lines.add(minilang_line);
    }

}
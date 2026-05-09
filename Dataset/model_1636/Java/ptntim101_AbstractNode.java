





import java.util.List;
import java.util.ArrayList;

public class ptntim101_AbstractNode  {

    private String name;
    private int tMax;
    private int tMin;





    private ptntim101_Place ptntim101_place;


    public ptntim101_AbstractNode(
        String name,        int tMax,        int tMin    ) {
        this.name = name;
        this.tMax = tMax;
        this.tMin = tMin;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getTmax() {
        return tMax;
    }

    public void setTmax(int tMax) {
        this.tMax = tMax;
    }
    public int getTmin() {
        return tMin;
    }

    public void setTmin(int tMin) {
        this.tMin = tMin;
    }

    public ptntim101_Place getPtntim101_place() {
        return ptntim101_place;
    }

    public void setPtntim101_place(ptntim101_Place ptntim101_place) {
        this.ptntim101_place = ptntim101_place;
    }

}
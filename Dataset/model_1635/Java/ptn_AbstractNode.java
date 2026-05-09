





import java.util.List;
import java.util.ArrayList;

public class ptn_AbstractNode  {

    private String name;
    private int tMin;
    private int tMax;





    private ptn_Place ptn_place;


    public ptn_AbstractNode(
        String name,        int tMin,        int tMax    ) {
        this.name = name;
        this.tMin = tMin;
        this.tMax = tMax;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getTmin() {
        return tMin;
    }

    public void setTmin(int tMin) {
        this.tMin = tMin;
    }
    public int getTmax() {
        return tMax;
    }

    public void setTmax(int tMax) {
        this.tMax = tMax;
    }

    public ptn_Place getPtn_place() {
        return ptn_place;
    }

    public void setPtn_place(ptn_Place ptn_place) {
        this.ptn_place = ptn_place;
    }

}
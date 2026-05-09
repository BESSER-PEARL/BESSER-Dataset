





import java.util.List;
import java.util.ArrayList;

public class drn_DepY_Impl extends Movement {

    private int tempsCST;
    private int distanceCST;
    private String name;



    public drn_DepY_Impl(
        int tempsCST,        int distanceCST,        String name    ) {
        super(
        );
        this.tempsCST = tempsCST;
        this.distanceCST = distanceCST;
        this.name = name;
    }


    public int getTempscst() {
        return tempsCST;
    }

    public void setTempscst(int tempsCST) {
        this.tempsCST = tempsCST;
    }
    public int getDistancecst() {
        return distanceCST;
    }

    public void setDistancecst(int distanceCST) {
        this.distanceCST = distanceCST;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
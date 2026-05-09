





import java.util.List;
import java.util.ArrayList;

public class drn_DepZ_Impl extends Movement {

    private String name;
    private int tempsCST;
    private int distanceCST;



    public drn_DepZ_Impl(
        String name,        int tempsCST,        int distanceCST    ) {
        super(
        );
        this.name = name;
        this.tempsCST = tempsCST;
        this.distanceCST = distanceCST;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
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


}
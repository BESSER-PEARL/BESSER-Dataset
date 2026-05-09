





import java.util.List;
import java.util.ArrayList;

public class drn_DepX_Impl extends Movement {

    private int tempsCST;
    private String name;
    private int distanceCST;



    public drn_DepX_Impl(
        int tempsCST,        String name,        int distanceCST    ) {
        super(
        );
        this.tempsCST = tempsCST;
        this.name = name;
        this.distanceCST = distanceCST;
    }


    public int getTempscst() {
        return tempsCST;
    }

    public void setTempscst(int tempsCST) {
        this.tempsCST = tempsCST;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getDistancecst() {
        return distanceCST;
    }

    public void setDistancecst(int distanceCST) {
        this.distanceCST = distanceCST;
    }


}
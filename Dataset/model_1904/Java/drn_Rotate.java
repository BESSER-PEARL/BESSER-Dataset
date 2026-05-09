





import java.util.List;
import java.util.ArrayList;

public class drn_Rotate extends Movement {

    private String name;
    private int tempsCST;
    private String angleCST;



    public drn_Rotate(
        String name,        int tempsCST,        String angleCST    ) {
        super(
        );
        this.name = name;
        this.tempsCST = tempsCST;
        this.angleCST = angleCST;
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
    public String getAnglecst() {
        return angleCST;
    }

    public void setAnglecst(String angleCST) {
        this.angleCST = angleCST;
    }


}
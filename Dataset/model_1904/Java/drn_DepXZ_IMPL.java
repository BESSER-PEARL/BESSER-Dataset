





import java.util.List;
import java.util.ArrayList;

public class drn_DepXZ_IMPL extends Movement {

    private int tempsCST;
    private String name;



    public drn_DepXZ_IMPL(
        int tempsCST,        String name    ) {
        super(
        );
        this.tempsCST = tempsCST;
        this.name = name;
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


}
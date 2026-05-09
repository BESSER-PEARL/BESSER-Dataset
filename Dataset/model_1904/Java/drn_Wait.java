





import java.util.List;
import java.util.ArrayList;

public class drn_Wait extends Movement {

    private String name;
    private int tempsCST;



    public drn_Wait(
        String name,        int tempsCST    ) {
        super(
        );
        this.name = name;
        this.tempsCST = tempsCST;
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


}
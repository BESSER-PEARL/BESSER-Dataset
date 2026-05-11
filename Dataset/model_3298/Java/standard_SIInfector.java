





import java.util.List;
import java.util.ArrayList;

public class standard_SIInfector extends StandardInfector {

    private float infectiousCount;



    public standard_SIInfector(
        float infectiousCount    ) {
        super(
        );
        this.infectiousCount = infectiousCount;
    }


    public float getInfectiouscount() {
        return infectiousCount;
    }

    public void setInfectiouscount(float infectiousCount) {
        this.infectiousCount = infectiousCount;
    }


}
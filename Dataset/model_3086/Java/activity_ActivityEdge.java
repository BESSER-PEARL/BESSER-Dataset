





import java.util.List;
import java.util.ArrayList;

public class activity_ActivityEdge extends ModelElement {

    private String kindOfRate;



    public activity_ActivityEdge(
        String kindOfRate    ) {
        super(
        );
        this.kindOfRate = kindOfRate;
    }


    public String getKindofrate() {
        return kindOfRate;
    }

    public void setKindofrate(String kindOfRate) {
        this.kindOfRate = kindOfRate;
    }


}
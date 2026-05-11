





import java.util.List;
import java.util.ArrayList;

public class systemmodel_GainBlock extends Block {

    private String gainfactor;



    public systemmodel_GainBlock(
        String gainfactor    ) {
        super(
        );
        this.gainfactor = gainfactor;
    }


    public String getGainfactor() {
        return gainfactor;
    }

    public void setGainfactor(String gainfactor) {
        this.gainfactor = gainfactor;
    }


}
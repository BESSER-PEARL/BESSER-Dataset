





import java.util.List;
import java.util.ArrayList;

public class model_Dunning extends Document {

    private String dunningLevel;



    public model_Dunning(
        String dunningLevel    ) {
        super(
        );
        this.dunningLevel = dunningLevel;
    }


    public String getDunninglevel() {
        return dunningLevel;
    }

    public void setDunninglevel(String dunningLevel) {
        this.dunningLevel = dunningLevel;
    }


}






import java.util.List;
import java.util.ArrayList;

public class dsl_ModelActor extends Actor {

    private String modelPath;
    private int scale;



    public dsl_ModelActor(
        String modelPath,        int scale    ) {
        super(
        );
        this.modelPath = modelPath;
        this.scale = scale;
    }


    public String getModelpath() {
        return modelPath;
    }

    public void setModelpath(String modelPath) {
        this.modelPath = modelPath;
    }
    public int getScale() {
        return scale;
    }

    public void setScale(int scale) {
        this.scale = scale;
    }


}






import java.util.List;
import java.util.ArrayList;

public class avm_eda_ExactLayoutConstraint extends PcbLayoutConstraint {

    private String Rotation;
    private String X;
    private String Y;
    private String Layer;



    public avm_eda_ExactLayoutConstraint(
        String Rotation,        String X,        String Y,        String Layer    ) {
        super(
        );
        this.Rotation = Rotation;
        this.X = X;
        this.Y = Y;
        this.Layer = Layer;
    }


    public String getRotation() {
        return Rotation;
    }

    public void setRotation(String Rotation) {
        this.Rotation = Rotation;
    }
    public String getX() {
        return X;
    }

    public void setX(String X) {
        this.X = X;
    }
    public String getY() {
        return Y;
    }

    public void setY(String Y) {
        this.Y = Y;
    }
    public String getLayer() {
        return Layer;
    }

    public void setLayer(String Layer) {
        this.Layer = Layer;
    }


}
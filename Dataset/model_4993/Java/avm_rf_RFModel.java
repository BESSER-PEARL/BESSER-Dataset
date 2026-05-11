





import java.util.List;
import java.util.ArrayList;

public class avm_rf_RFModel extends DomainModel_ {

    private String Rotation;
    private String Y;
    private String X;



    public avm_rf_RFModel(
        String Rotation,        String Y,        String X    ) {
        super(
        );
        this.Rotation = Rotation;
        this.Y = Y;
        this.X = X;
    }


    public String getRotation() {
        return Rotation;
    }

    public void setRotation(String Rotation) {
        this.Rotation = Rotation;
    }
    public String getY() {
        return Y;
    }

    public void setY(String Y) {
        this.Y = Y;
    }
    public String getX() {
        return X;
    }

    public void setX(String X) {
        this.X = X;
    }


}
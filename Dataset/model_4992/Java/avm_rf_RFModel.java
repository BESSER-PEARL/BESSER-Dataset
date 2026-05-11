





import java.util.List;
import java.util.ArrayList;

public class avm_rf_RFModel extends DomainModel_ {

    private String Rotation;
    private String X;
    private String Y;



    public avm_rf_RFModel(
        String Rotation,        String X,        String Y    ) {
        super(
        );
        this.Rotation = Rotation;
        this.X = X;
        this.Y = Y;
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


}
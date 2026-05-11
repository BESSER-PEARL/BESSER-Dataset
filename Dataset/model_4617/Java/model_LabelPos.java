





import java.util.List;
import java.util.ArrayList;

public class model_LabelPos extends OnoObject {

    private int posX;
    private int posY;



    public model_LabelPos(
        int posX,        int posY    ) {
        super(
        );
        this.posX = posX;
        this.posY = posY;
    }


    public int getPosx() {
        return posX;
    }

    public void setPosx(int posX) {
        this.posX = posX;
    }
    public int getPosy() {
        return posY;
    }

    public void setPosy(int posY) {
        this.posY = posY;
    }


}
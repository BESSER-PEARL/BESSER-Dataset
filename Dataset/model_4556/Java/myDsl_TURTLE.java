





import java.util.List;
import java.util.ArrayList;

public class myDsl_TURTLE extends CMD {

    private int startPosX;
    private int startPosY;



    public myDsl_TURTLE(
        int startPosX,        int startPosY    ) {
        super(
        );
        this.startPosX = startPosX;
        this.startPosY = startPosY;
    }


    public int getStartposx() {
        return startPosX;
    }

    public void setStartposx(int startPosX) {
        this.startPosX = startPosX;
    }
    public int getStartposy() {
        return startPosY;
    }

    public void setStartposy(int startPosY) {
        this.startPosY = startPosY;
    }


}






import java.util.List;
import java.util.ArrayList;

public class shr5_ActiveMatixDevice extends MatrixAttributes {

    private int angriff;
    private int schleicher;



    public shr5_ActiveMatixDevice(
        int angriff,        int schleicher    ) {
        super(
        );
        this.angriff = angriff;
        this.schleicher = schleicher;
    }


    public int getAngriff() {
        return angriff;
    }

    public void setAngriff(int angriff) {
        this.angriff = angriff;
    }
    public int getSchleicher() {
        return schleicher;
    }

    public void setSchleicher(int schleicher) {
        this.schleicher = schleicher;
    }


}
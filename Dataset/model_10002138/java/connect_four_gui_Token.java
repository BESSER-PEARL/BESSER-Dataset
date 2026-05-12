





import java.util.List;
import java.util.ArrayList;

public class connect_four_gui_Token  {

    private String Y;
    private String X;
    private boolean red;



    public connect_four_gui_Token(
        String Y,        String X,        boolean red    ) {
        this.Y = Y;
        this.X = X;
        this.red = red;
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
    public boolean getRed() {
        return red;
    }

    public void setRed(boolean red) {
        this.red = red;
    }


}
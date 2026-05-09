





import java.util.List;
import java.util.ArrayList;

public class uma_Polyline extends GraphicPrimitive {

    private String closed;



    public uma_Polyline(
        String closed    ) {
        super(
        );
        this.closed = closed;
    }


    public String getClosed() {
        return closed;
    }

    public void setClosed(String closed) {
        this.closed = closed;
    }


}
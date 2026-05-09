





import java.util.List;
import java.util.ArrayList;

public class book_Fade extends Animation {

    private float fromValue;
    private float toValue;



    public book_Fade(
        float fromValue,        float toValue    ) {
        super(
        );
        this.fromValue = fromValue;
        this.toValue = toValue;
    }


    public float getFromvalue() {
        return fromValue;
    }

    public void setFromvalue(float fromValue) {
        this.fromValue = fromValue;
    }
    public float getTovalue() {
        return toValue;
    }

    public void setTovalue(float toValue) {
        this.toValue = toValue;
    }


}
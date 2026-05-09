





import java.util.List;
import java.util.ArrayList;

public class ptnet_Uniform extends Distribution {

    private float Lower;
    private float Upper;



    public ptnet_Uniform(
        float Lower,        float Upper    ) {
        super(
        );
        this.Lower = Lower;
        this.Upper = Upper;
    }


    public float getLower() {
        return Lower;
    }

    public void setLower(float Lower) {
        this.Lower = Lower;
    }
    public float getUpper() {
        return Upper;
    }

    public void setUpper(float Upper) {
        this.Upper = Upper;
    }


}
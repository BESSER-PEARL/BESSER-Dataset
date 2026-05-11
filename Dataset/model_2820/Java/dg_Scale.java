





import java.util.List;
import java.util.ArrayList;

public class dg_Scale extends Transform {

    private String factorX;
    private String factorY;



    public dg_Scale(
        String factorX,        String factorY    ) {
        super(
        );
        this.factorX = factorX;
        this.factorY = factorY;
    }


    public String getFactorx() {
        return factorX;
    }

    public void setFactorx(String factorX) {
        this.factorX = factorX;
    }
    public String getFactory() {
        return factorY;
    }

    public void setFactory(String factorY) {
        this.factorY = factorY;
    }


}
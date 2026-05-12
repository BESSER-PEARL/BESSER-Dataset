





import java.util.List;
import java.util.ArrayList;

public class Cuadrado  {

    private String img;
    private int v2;
    private int v1;



    public Cuadrado(
        String img,        int v2,        int v1    ) {
        this.img = img;
        this.v2 = v2;
        this.v1 = v1;
    }


    public String getImg() {
        return img;
    }

    public void setImg(String img) {
        this.img = img;
    }
    public int getV2() {
        return v2;
    }

    public void setV2(int v2) {
        this.v2 = v2;
    }
    public int getV1() {
        return v1;
    }

    public void setV1(int v1) {
        this.v1 = v1;
    }


}
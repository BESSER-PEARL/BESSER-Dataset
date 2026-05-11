





import java.util.List;
import java.util.ArrayList;

public class model3_Image  {

    private String data;
    private int width;
    private int height;



    public model3_Image(
        String data,        int width,        int height    ) {
        this.data = data;
        this.width = width;
        this.height = height;
    }


    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }


}
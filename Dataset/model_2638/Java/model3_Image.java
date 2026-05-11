





import java.util.List;
import java.util.ArrayList;

public class model3_Image  {

    private int height;
    private String data;
    private int width;



    public model3_Image(
        int height,        String data,        int width    ) {
        this.height = height;
        this.data = data;
        this.width = width;
    }


    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
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


}
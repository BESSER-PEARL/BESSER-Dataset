





import java.util.List;
import java.util.ArrayList;

public class rental_Device extends RentalObject {

    private int height;
    private int width;
    private int length;
    private String serialNumber;



    public rental_Device(
        int height,        int width,        int length,        String serialNumber    ) {
        super(
        );
        this.height = height;
        this.width = width;
        this.length = length;
        this.serialNumber = serialNumber;
    }


    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public String getSerialnumber() {
        return serialNumber;
    }

    public void setSerialnumber(String serialNumber) {
        this.serialNumber = serialNumber;
    }


}
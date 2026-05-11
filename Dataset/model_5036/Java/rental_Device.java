





import java.util.List;
import java.util.ArrayList;

public class rental_Device extends RentalObject {

    private int height;
    private String serialNumber;
    private int length;
    private int width;



    public rental_Device(
        int height,        String serialNumber,        int length,        int width    ) {
        super(
        );
        this.height = height;
        this.serialNumber = serialNumber;
        this.length = length;
        this.width = width;
    }


    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public String getSerialnumber() {
        return serialNumber;
    }

    public void setSerialnumber(String serialNumber) {
        this.serialNumber = serialNumber;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }


}
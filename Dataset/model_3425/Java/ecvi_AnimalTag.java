





import java.util.List;
import java.util.ArrayList;

public class ecvi_AnimalTag  {

    private String brandImage;
    private String number;
    private String type;





    private ecvi_Animal ecvi_animal;


    public ecvi_AnimalTag(
        String brandImage,        String number,        String type    ) {
        this.brandImage = brandImage;
        this.number = number;
        this.type = type;
    }


    public String getBrandimage() {
        return brandImage;
    }

    public void setBrandimage(String brandImage) {
        this.brandImage = brandImage;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public ecvi_Animal getEcvi_animal() {
        return ecvi_animal;
    }

    public void setEcvi_animal(ecvi_Animal ecvi_animal) {
        this.ecvi_animal = ecvi_animal;
    }

}
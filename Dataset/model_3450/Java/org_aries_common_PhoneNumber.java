





import java.util.List;
import java.util.ArrayList;

public class org_aries_common_PhoneNumber  {

    private String country;
    private String value;
    private String number;
    private String id;
    private String area;
    private String extension;
    private String type;



    public org_aries_common_PhoneNumber(
        String country,        String value,        String number,        String id,        String area,        String extension,        String type    ) {
        this.country = country;
        this.value = value;
        this.number = number;
        this.id = id;
        this.area = area;
        this.extension = extension;
        this.type = type;
    }


    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getArea() {
        return area;
    }

    public void setArea(String area) {
        this.area = area;
    }
    public String getExtension() {
        return extension;
    }

    public void setExtension(String extension) {
        this.extension = extension;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}
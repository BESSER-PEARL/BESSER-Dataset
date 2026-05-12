





import java.util.List;
import java.util.ArrayList;

public class Address  {

    private String Line1;
    private String City;
    private String Line_2;
    private String County;



    public Address(
        String Line1,        String City,        String Line_2,        String County    ) {
        this.Line1 = Line1;
        this.City = City;
        this.Line_2 = Line_2;
        this.County = County;
    }


    public String getLine1() {
        return Line1;
    }

    public void setLine1(String Line1) {
        this.Line1 = Line1;
    }
    public String getCity() {
        return City;
    }

    public void setCity(String City) {
        this.City = City;
    }
    public String getLine_2() {
        return Line_2;
    }

    public void setLine_2(String Line_2) {
        this.Line_2 = Line_2;
    }
    public String getCounty() {
        return County;
    }

    public void setCounty(String County) {
        this.County = County;
    }


}
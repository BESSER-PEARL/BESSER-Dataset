





import java.util.List;
import java.util.ArrayList;

public class decobat_Service  {

    private String hourlyCostPrice;
    private String name;
    private String code;
    private String hourlyBilledPrice;
    private String shortDescription;
    private String description;



    public decobat_Service(
        String hourlyCostPrice,        String name,        String code,        String hourlyBilledPrice,        String shortDescription,        String description    ) {
        this.hourlyCostPrice = hourlyCostPrice;
        this.name = name;
        this.code = code;
        this.hourlyBilledPrice = hourlyBilledPrice;
        this.shortDescription = shortDescription;
        this.description = description;
    }


    public String getHourlycostprice() {
        return hourlyCostPrice;
    }

    public void setHourlycostprice(String hourlyCostPrice) {
        this.hourlyCostPrice = hourlyCostPrice;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getHourlybilledprice() {
        return hourlyBilledPrice;
    }

    public void setHourlybilledprice(String hourlyBilledPrice) {
        this.hourlyBilledPrice = hourlyBilledPrice;
    }
    public String getShortdescription() {
        return shortDescription;
    }

    public void setShortdescription(String shortDescription) {
        this.shortDescription = shortDescription;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}






import java.util.List;
import java.util.ArrayList;

public class decobat_Service  {

    private String hourlyBilledPrice;
    private String description;
    private String code;
    private String shortDescription;
    private String name;
    private String hourlyCostPrice;



    public decobat_Service(
        String hourlyBilledPrice,        String description,        String code,        String shortDescription,        String name,        String hourlyCostPrice    ) {
        this.hourlyBilledPrice = hourlyBilledPrice;
        this.description = description;
        this.code = code;
        this.shortDescription = shortDescription;
        this.name = name;
        this.hourlyCostPrice = hourlyCostPrice;
    }


    public String getHourlybilledprice() {
        return hourlyBilledPrice;
    }

    public void setHourlybilledprice(String hourlyBilledPrice) {
        this.hourlyBilledPrice = hourlyBilledPrice;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getShortdescription() {
        return shortDescription;
    }

    public void setShortdescription(String shortDescription) {
        this.shortDescription = shortDescription;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getHourlycostprice() {
        return hourlyCostPrice;
    }

    public void setHourlycostprice(String hourlyCostPrice) {
        this.hourlyCostPrice = hourlyCostPrice;
    }


}
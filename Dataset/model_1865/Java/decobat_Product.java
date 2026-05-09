




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class decobat_Product  {

    private LocalDate update;
    private String width;
    private String name;
    private String shortDescription;
    private String depth;
    private String unitWeight;
    private String unitBilledPrice;
    private String description;
    private LocalDate created;
    private String height;
    private String unitCostPrice;



    public decobat_Product(
        LocalDate update,        String width,        String name,        String shortDescription,        String depth,        String unitWeight,        String unitBilledPrice,        String description,        LocalDate created,        String height,        String unitCostPrice    ) {
        this.update = update;
        this.width = width;
        this.name = name;
        this.shortDescription = shortDescription;
        this.depth = depth;
        this.unitWeight = unitWeight;
        this.unitBilledPrice = unitBilledPrice;
        this.description = description;
        this.created = created;
        this.height = height;
        this.unitCostPrice = unitCostPrice;
    }


    public LocalDate getUpdate() {
        return update;
    }

    public void setUpdate(LocalDate update) {
        this.update = update;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getShortdescription() {
        return shortDescription;
    }

    public void setShortdescription(String shortDescription) {
        this.shortDescription = shortDescription;
    }
    public String getDepth() {
        return depth;
    }

    public void setDepth(String depth) {
        this.depth = depth;
    }
    public String getUnitweight() {
        return unitWeight;
    }

    public void setUnitweight(String unitWeight) {
        this.unitWeight = unitWeight;
    }
    public String getUnitbilledprice() {
        return unitBilledPrice;
    }

    public void setUnitbilledprice(String unitBilledPrice) {
        this.unitBilledPrice = unitBilledPrice;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getUnitcostprice() {
        return unitCostPrice;
    }

    public void setUnitcostprice(String unitCostPrice) {
        this.unitCostPrice = unitCostPrice;
    }


}
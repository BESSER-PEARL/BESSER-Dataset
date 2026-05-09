




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class decobat_Product  {

    private LocalDate update;
    private String width;
    private String name;
    private LocalDate created;
    private String unitBilledPrice;
    private String unitWeight;
    private String unitCostPrice;
    private String depth;
    private String height;
    private String description;
    private String shortDescription;



    public decobat_Product(
        LocalDate update,        String width,        String name,        LocalDate created,        String unitBilledPrice,        String unitWeight,        String unitCostPrice,        String depth,        String height,        String description,        String shortDescription    ) {
        this.update = update;
        this.width = width;
        this.name = name;
        this.created = created;
        this.unitBilledPrice = unitBilledPrice;
        this.unitWeight = unitWeight;
        this.unitCostPrice = unitCostPrice;
        this.depth = depth;
        this.height = height;
        this.description = description;
        this.shortDescription = shortDescription;
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
    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }
    public String getUnitbilledprice() {
        return unitBilledPrice;
    }

    public void setUnitbilledprice(String unitBilledPrice) {
        this.unitBilledPrice = unitBilledPrice;
    }
    public String getUnitweight() {
        return unitWeight;
    }

    public void setUnitweight(String unitWeight) {
        this.unitWeight = unitWeight;
    }
    public String getUnitcostprice() {
        return unitCostPrice;
    }

    public void setUnitcostprice(String unitCostPrice) {
        this.unitCostPrice = unitCostPrice;
    }
    public String getDepth() {
        return depth;
    }

    public void setDepth(String depth) {
        this.depth = depth;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getShortdescription() {
        return shortDescription;
    }

    public void setShortdescription(String shortDescription) {
        this.shortDescription = shortDescription;
    }


}
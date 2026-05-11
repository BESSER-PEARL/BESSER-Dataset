




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_DocumentItem extends IEntity {

    private String posNr;
    private String optional;
    private String picture;
    private String quantityUnit;
    private LocalDate vestingPeriodStart;
    private LocalDate vestingPeriodEnd;
    private String quantity;
    private String tara;
    private String itemType;
    private String price;
    private String noVat;
    private String description;
    private String itemNumber;
    private String weight;
    private String gtin;
    private String originQuantity;
    private String itemRebate;





    private model_VAT model_vat;




    private model_Document model_document;


    public model_DocumentItem(
        String posNr,        String optional,        String picture,        String quantityUnit,        LocalDate vestingPeriodStart,        LocalDate vestingPeriodEnd,        String quantity,        String tara,        String itemType,        String price,        String noVat,        String description,        String itemNumber,        String weight,        String gtin,        String originQuantity,        String itemRebate    ) {
        super(
        );
        this.posNr = posNr;
        this.optional = optional;
        this.picture = picture;
        this.quantityUnit = quantityUnit;
        this.vestingPeriodStart = vestingPeriodStart;
        this.vestingPeriodEnd = vestingPeriodEnd;
        this.quantity = quantity;
        this.tara = tara;
        this.itemType = itemType;
        this.price = price;
        this.noVat = noVat;
        this.description = description;
        this.itemNumber = itemNumber;
        this.weight = weight;
        this.gtin = gtin;
        this.originQuantity = originQuantity;
        this.itemRebate = itemRebate;
    }


    public String getPosnr() {
        return posNr;
    }

    public void setPosnr(String posNr) {
        this.posNr = posNr;
    }
    public String getOptional() {
        return optional;
    }

    public void setOptional(String optional) {
        this.optional = optional;
    }
    public String getPicture() {
        return picture;
    }

    public void setPicture(String picture) {
        this.picture = picture;
    }
    public String getQuantityunit() {
        return quantityUnit;
    }

    public void setQuantityunit(String quantityUnit) {
        this.quantityUnit = quantityUnit;
    }
    public LocalDate getVestingperiodstart() {
        return vestingPeriodStart;
    }

    public void setVestingperiodstart(LocalDate vestingPeriodStart) {
        this.vestingPeriodStart = vestingPeriodStart;
    }
    public LocalDate getVestingperiodend() {
        return vestingPeriodEnd;
    }

    public void setVestingperiodend(LocalDate vestingPeriodEnd) {
        this.vestingPeriodEnd = vestingPeriodEnd;
    }
    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }
    public String getTara() {
        return tara;
    }

    public void setTara(String tara) {
        this.tara = tara;
    }
    public String getItemtype() {
        return itemType;
    }

    public void setItemtype(String itemType) {
        this.itemType = itemType;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getNovat() {
        return noVat;
    }

    public void setNovat(String noVat) {
        this.noVat = noVat;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getItemnumber() {
        return itemNumber;
    }

    public void setItemnumber(String itemNumber) {
        this.itemNumber = itemNumber;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getGtin() {
        return gtin;
    }

    public void setGtin(String gtin) {
        this.gtin = gtin;
    }
    public String getOriginquantity() {
        return originQuantity;
    }

    public void setOriginquantity(String originQuantity) {
        this.originQuantity = originQuantity;
    }
    public String getItemrebate() {
        return itemRebate;
    }

    public void setItemrebate(String itemRebate) {
        this.itemRebate = itemRebate;
    }

    public model_VAT getModel_vat() {
        return model_vat;
    }

    public void setModel_vat(model_VAT model_vat) {
        this.model_vat = model_vat;
    }
    public model_Document getModel_document() {
        return model_document;
    }

    public void setModel_document(model_Document model_document) {
        this.model_document = model_document;
    }

}
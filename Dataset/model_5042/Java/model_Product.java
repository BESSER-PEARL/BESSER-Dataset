





import java.util.List;
import java.util.ArrayList;

public class model_Product extends IDescribableEntity {

    private String cdf01;
    private String price5;
    private String cdf03;
    private String block2;
    private String weight;
    private String costPrice;
    private String block4;
    private String block1;
    private String picture;
    private String block3;
    private String webshopId;
    private String cdf02;
    private String price1;
    private String price4;
    private String price2;
    private String itemNumber;
    private String gtin;
    private String price3;
    private String quantity;
    private String sellingUnit;
    private String block5;
    private String quantityUnit;





    private model_VAT model_vat;




    private model_ProductCategory model_productcategory;




    private List<model_ProductOptions> model_productoptionss;




    private List<model_ProductBlockPrice> model_productblockprices;




    private model_DocumentItem model_documentitem;


    public model_Product(
        String cdf01,        String price5,        String cdf03,        String block2,        String weight,        String costPrice,        String block4,        String block1,        String picture,        String block3,        String webshopId,        String cdf02,        String price1,        String price4,        String price2,        String itemNumber,        String gtin,        String price3,        String quantity,        String sellingUnit,        String block5,        String quantityUnit    ) {
        super(
        );
        this.cdf01 = cdf01;
        this.price5 = price5;
        this.cdf03 = cdf03;
        this.block2 = block2;
        this.weight = weight;
        this.costPrice = costPrice;
        this.block4 = block4;
        this.block1 = block1;
        this.picture = picture;
        this.block3 = block3;
        this.webshopId = webshopId;
        this.cdf02 = cdf02;
        this.price1 = price1;
        this.price4 = price4;
        this.price2 = price2;
        this.itemNumber = itemNumber;
        this.gtin = gtin;
        this.price3 = price3;
        this.quantity = quantity;
        this.sellingUnit = sellingUnit;
        this.block5 = block5;
        this.quantityUnit = quantityUnit;
        this.model_productoptionss = new ArrayList<>();
        this.model_productblockprices = new ArrayList<>();
    }

    public model_Product(
        String cdf01,        String price5,        String cdf03,        String block2,        String weight,        String costPrice,        String block4,        String block1,        String picture,        String block3,        String webshopId,        String cdf02,        String price1,        String price4,        String price2,        String itemNumber,        String gtin,        String price3,        String quantity,        String sellingUnit,        String block5,        String quantityUnit        ArrayList<model_ProductOptions> model_productoptionss,        ArrayList<model_ProductBlockPrice> model_productblockprices    ) {
        this.cdf01 = cdf01;
        this.price5 = price5;
        this.cdf03 = cdf03;
        this.block2 = block2;
        this.weight = weight;
        this.costPrice = costPrice;
        this.block4 = block4;
        this.block1 = block1;
        this.picture = picture;
        this.block3 = block3;
        this.webshopId = webshopId;
        this.cdf02 = cdf02;
        this.price1 = price1;
        this.price4 = price4;
        this.price2 = price2;
        this.itemNumber = itemNumber;
        this.gtin = gtin;
        this.price3 = price3;
        this.quantity = quantity;
        this.sellingUnit = sellingUnit;
        this.block5 = block5;
        this.quantityUnit = quantityUnit;
        this.model_productoptionss = model_productoptionss;
        this.model_productblockprices = model_productblockprices;
    }

    public String getCdf01() {
        return cdf01;
    }

    public void setCdf01(String cdf01) {
        this.cdf01 = cdf01;
    }
    public String getPrice5() {
        return price5;
    }

    public void setPrice5(String price5) {
        this.price5 = price5;
    }
    public String getCdf03() {
        return cdf03;
    }

    public void setCdf03(String cdf03) {
        this.cdf03 = cdf03;
    }
    public String getBlock2() {
        return block2;
    }

    public void setBlock2(String block2) {
        this.block2 = block2;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getCostprice() {
        return costPrice;
    }

    public void setCostprice(String costPrice) {
        this.costPrice = costPrice;
    }
    public String getBlock4() {
        return block4;
    }

    public void setBlock4(String block4) {
        this.block4 = block4;
    }
    public String getBlock1() {
        return block1;
    }

    public void setBlock1(String block1) {
        this.block1 = block1;
    }
    public String getPicture() {
        return picture;
    }

    public void setPicture(String picture) {
        this.picture = picture;
    }
    public String getBlock3() {
        return block3;
    }

    public void setBlock3(String block3) {
        this.block3 = block3;
    }
    public String getWebshopid() {
        return webshopId;
    }

    public void setWebshopid(String webshopId) {
        this.webshopId = webshopId;
    }
    public String getCdf02() {
        return cdf02;
    }

    public void setCdf02(String cdf02) {
        this.cdf02 = cdf02;
    }
    public String getPrice1() {
        return price1;
    }

    public void setPrice1(String price1) {
        this.price1 = price1;
    }
    public String getPrice4() {
        return price4;
    }

    public void setPrice4(String price4) {
        this.price4 = price4;
    }
    public String getPrice2() {
        return price2;
    }

    public void setPrice2(String price2) {
        this.price2 = price2;
    }
    public String getItemnumber() {
        return itemNumber;
    }

    public void setItemnumber(String itemNumber) {
        this.itemNumber = itemNumber;
    }
    public String getGtin() {
        return gtin;
    }

    public void setGtin(String gtin) {
        this.gtin = gtin;
    }
    public String getPrice3() {
        return price3;
    }

    public void setPrice3(String price3) {
        this.price3 = price3;
    }
    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }
    public String getSellingunit() {
        return sellingUnit;
    }

    public void setSellingunit(String sellingUnit) {
        this.sellingUnit = sellingUnit;
    }
    public String getBlock5() {
        return block5;
    }

    public void setBlock5(String block5) {
        this.block5 = block5;
    }
    public String getQuantityunit() {
        return quantityUnit;
    }

    public void setQuantityunit(String quantityUnit) {
        this.quantityUnit = quantityUnit;
    }

    public model_VAT getModel_vat() {
        return model_vat;
    }

    public void setModel_vat(model_VAT model_vat) {
        this.model_vat = model_vat;
    }
    public model_ProductCategory getModel_productcategory() {
        return model_productcategory;
    }

    public void setModel_productcategory(model_ProductCategory model_productcategory) {
        this.model_productcategory = model_productcategory;
    }
    public List<model_ProductOptions> getModel_productoptionss() {
        return model_productoptionss;
    }

    public void addModel_productoptions(Model_productoptions model_productoptions) {
        this.model_productoptionss.add(model_productoptions);
    }
    public List<model_ProductBlockPrice> getModel_productblockprices() {
        return model_productblockprices;
    }

    public void addModel_productblockprice(Model_productblockprice model_productblockprice) {
        this.model_productblockprices.add(model_productblockprice);
    }
    public model_DocumentItem getModel_documentitem() {
        return model_documentitem;
    }

    public void setModel_documentitem(model_DocumentItem model_documentitem) {
        this.model_documentitem = model_documentitem;
    }

}
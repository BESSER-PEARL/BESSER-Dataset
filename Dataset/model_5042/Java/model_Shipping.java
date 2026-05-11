





import java.util.List;
import java.util.ArrayList;

public class model_Shipping extends IDescribableEntity {

    private String shippingValue;
    private String code;
    private String autoVat;





    private model_Document model_document;




    private model_ShippingCategory model_shippingcategory;




    private model_VAT model_vat;


    public model_Shipping(
        String shippingValue,        String code,        String autoVat    ) {
        super(
        );
        this.shippingValue = shippingValue;
        this.code = code;
        this.autoVat = autoVat;
    }


    public String getShippingvalue() {
        return shippingValue;
    }

    public void setShippingvalue(String shippingValue) {
        this.shippingValue = shippingValue;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getAutovat() {
        return autoVat;
    }

    public void setAutovat(String autoVat) {
        this.autoVat = autoVat;
    }

    public model_Document getModel_document() {
        return model_document;
    }

    public void setModel_document(model_Document model_document) {
        this.model_document = model_document;
    }
    public model_ShippingCategory getModel_shippingcategory() {
        return model_shippingcategory;
    }

    public void setModel_shippingcategory(model_ShippingCategory model_shippingcategory) {
        this.model_shippingcategory = model_shippingcategory;
    }
    public model_VAT getModel_vat() {
        return model_vat;
    }

    public void setModel_vat(model_VAT model_vat) {
        this.model_vat = model_vat;
    }

}
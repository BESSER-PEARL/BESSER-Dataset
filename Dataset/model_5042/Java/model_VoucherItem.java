





import java.util.List;
import java.util.ArrayList;

public class model_VoucherItem extends IEntity {

    private String price;
    private String posNr;
    private String itemVoucherType;





    private model_ItemAccountType model_itemaccounttype;




    private model_VAT model_vat;




    private model_Voucher model_voucher;


    public model_VoucherItem(
        String price,        String posNr,        String itemVoucherType    ) {
        super(
        );
        this.price = price;
        this.posNr = posNr;
        this.itemVoucherType = itemVoucherType;
    }


    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getPosnr() {
        return posNr;
    }

    public void setPosnr(String posNr) {
        this.posNr = posNr;
    }
    public String getItemvouchertype() {
        return itemVoucherType;
    }

    public void setItemvouchertype(String itemVoucherType) {
        this.itemVoucherType = itemVoucherType;
    }

    public model_ItemAccountType getModel_itemaccounttype() {
        return model_itemaccounttype;
    }

    public void setModel_itemaccounttype(model_ItemAccountType model_itemaccounttype) {
        this.model_itemaccounttype = model_itemaccounttype;
    }
    public model_VAT getModel_vat() {
        return model_vat;
    }

    public void setModel_vat(model_VAT model_vat) {
        this.model_vat = model_vat;
    }
    public model_Voucher getModel_voucher() {
        return model_voucher;
    }

    public void setModel_voucher(model_Voucher model_voucher) {
        this.model_voucher = model_voucher;
    }

}
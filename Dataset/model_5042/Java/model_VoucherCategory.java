





import java.util.List;
import java.util.ArrayList;

public class model_VoucherCategory extends AbstractCategory {






    private model_Payment model_payment;




    private model_Voucher model_voucher;


    public model_VoucherCategory(
    ) {
        super(
        );
    }



    public model_Payment getModel_payment() {
        return model_payment;
    }

    public void setModel_payment(model_Payment model_payment) {
        this.model_payment = model_payment;
    }
    public model_Voucher getModel_voucher() {
        return model_voucher;
    }

    public void setModel_voucher(model_Voucher model_voucher) {
        this.model_voucher = model_voucher;
    }

}
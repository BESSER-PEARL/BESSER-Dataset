





import java.util.List;
import java.util.ArrayList;

public class model_Payment extends IEntity {

    private String discountDays;
    private String unpaidText;
    private String discountValue;
    private String code;
    private String depositText;
    private String paidText;
    private String description;
    private String netDays;



    public model_Payment(
        String discountDays,        String unpaidText,        String discountValue,        String code,        String depositText,        String paidText,        String description,        String netDays    ) {
        super(
        );
        this.discountDays = discountDays;
        this.unpaidText = unpaidText;
        this.discountValue = discountValue;
        this.code = code;
        this.depositText = depositText;
        this.paidText = paidText;
        this.description = description;
        this.netDays = netDays;
    }


    public String getDiscountdays() {
        return discountDays;
    }

    public void setDiscountdays(String discountDays) {
        this.discountDays = discountDays;
    }
    public String getUnpaidtext() {
        return unpaidText;
    }

    public void setUnpaidtext(String unpaidText) {
        this.unpaidText = unpaidText;
    }
    public String getDiscountvalue() {
        return discountValue;
    }

    public void setDiscountvalue(String discountValue) {
        this.discountValue = discountValue;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getDeposittext() {
        return depositText;
    }

    public void setDeposittext(String depositText) {
        this.depositText = depositText;
    }
    public String getPaidtext() {
        return paidText;
    }

    public void setPaidtext(String paidText) {
        this.paidText = paidText;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getNetdays() {
        return netDays;
    }

    public void setNetdays(String netDays) {
        this.netDays = netDays;
    }


}
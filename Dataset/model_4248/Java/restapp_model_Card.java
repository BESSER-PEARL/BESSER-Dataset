




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class restapp_model_Card  {

    private int id;
    private float payedValue;
    private float totalValue;
    private LocalDate sellDate;
    private int discount;
    private float totalValueWithDiscount;
    private float change;



    public restapp_model_Card(
        int id,        float payedValue,        float totalValue,        LocalDate sellDate,        int discount,        float totalValueWithDiscount,        float change    ) {
        this.id = id;
        this.payedValue = payedValue;
        this.totalValue = totalValue;
        this.sellDate = sellDate;
        this.discount = discount;
        this.totalValueWithDiscount = totalValueWithDiscount;
        this.change = change;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public float getPayedvalue() {
        return payedValue;
    }

    public void setPayedvalue(float payedValue) {
        this.payedValue = payedValue;
    }
    public float getTotalvalue() {
        return totalValue;
    }

    public void setTotalvalue(float totalValue) {
        this.totalValue = totalValue;
    }
    public LocalDate getSelldate() {
        return sellDate;
    }

    public void setSelldate(LocalDate sellDate) {
        this.sellDate = sellDate;
    }
    public int getDiscount() {
        return discount;
    }

    public void setDiscount(int discount) {
        this.discount = discount;
    }
    public float getTotalvaluewithdiscount() {
        return totalValueWithDiscount;
    }

    public void setTotalvaluewithdiscount(float totalValueWithDiscount) {
        this.totalValueWithDiscount = totalValueWithDiscount;
    }
    public float getChange() {
        return change;
    }

    public void setChange(float change) {
        this.change = change;
    }


}
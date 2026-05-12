





import java.util.List;
import java.util.ArrayList;

public class Price  {

    private String ActualPrice;





    private Price price;


    public Price(
        String ActualPrice    ) {
        this.ActualPrice = ActualPrice;
    }


    public String getActualprice() {
        return ActualPrice;
    }

    public void setActualprice(String ActualPrice) {
        this.ActualPrice = ActualPrice;
    }

    public Price getPrice() {
        return price;
    }

    public void setPrice(Price price) {
        this.price = price;
    }

}
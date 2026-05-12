





import java.util.List;
import java.util.ArrayList;

public class Report  {

    private String profit;
    private String totalSales;
    private String orders;



    public Report(
        String profit,        String totalSales,        String orders    ) {
        this.profit = profit;
        this.totalSales = totalSales;
        this.orders = orders;
    }


    public String getProfit() {
        return profit;
    }

    public void setProfit(String profit) {
        this.profit = profit;
    }
    public String getTotalsales() {
        return totalSales;
    }

    public void setTotalsales(String totalSales) {
        this.totalSales = totalSales;
    }
    public String getOrders() {
        return orders;
    }

    public void setOrders(String orders) {
        this.orders = orders;
    }


}
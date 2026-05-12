





import java.util.List;
import java.util.ArrayList;

public class Report  {

    private String profit;
    private String orders;
    private String totalSales;





    private RMS rms;


    public Report(
        String profit,        String orders,        String totalSales    ) {
        this.profit = profit;
        this.orders = orders;
        this.totalSales = totalSales;
    }


    public String getProfit() {
        return profit;
    }

    public void setProfit(String profit) {
        this.profit = profit;
    }
    public String getOrders() {
        return orders;
    }

    public void setOrders(String orders) {
        this.orders = orders;
    }
    public String getTotalsales() {
        return totalSales;
    }

    public void setTotalsales(String totalSales) {
        this.totalSales = totalSales;
    }

    public RMS getRms() {
        return rms;
    }

    public void setRms(RMS rms) {
        this.rms = rms;
    }

}
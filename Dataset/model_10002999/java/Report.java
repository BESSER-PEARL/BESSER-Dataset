





import java.util.List;
import java.util.ArrayList;

public class Report  {

    private String totalSales;
    private String orders;
    private String profit;





    private RMS rms;


    public Report(
        String totalSales,        String orders,        String profit    ) {
        this.totalSales = totalSales;
        this.orders = orders;
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
    public String getProfit() {
        return profit;
    }

    public void setProfit(String profit) {
        this.profit = profit;
    }

    public RMS getRms() {
        return rms;
    }

    public void setRms(RMS rms) {
        this.rms = rms;
    }

}
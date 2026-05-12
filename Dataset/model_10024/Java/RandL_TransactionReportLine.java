





import java.util.List;
import java.util.ArrayList;

public class RandL_TransactionReportLine  {

    private String points;
    private String serviceDesc;
    private String partnerName;
    private String amount;





    private RandL_Date randl_date;




    private RandL_Transaction randl_transaction;


    public RandL_TransactionReportLine(
        String points,        String serviceDesc,        String partnerName,        String amount    ) {
        this.points = points;
        this.serviceDesc = serviceDesc;
        this.partnerName = partnerName;
        this.amount = amount;
    }


    public String getPoints() {
        return points;
    }

    public void setPoints(String points) {
        this.points = points;
    }
    public String getServicedesc() {
        return serviceDesc;
    }

    public void setServicedesc(String serviceDesc) {
        this.serviceDesc = serviceDesc;
    }
    public String getPartnername() {
        return partnerName;
    }

    public void setPartnername(String partnerName) {
        this.partnerName = partnerName;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }

    public RandL_Date getRandl_date() {
        return randl_date;
    }

    public void setRandl_date(RandL_Date randl_date) {
        this.randl_date = randl_date;
    }
    public RandL_Transaction getRandl_transaction() {
        return randl_transaction;
    }

    public void setRandl_transaction(RandL_Transaction randl_transaction) {
        this.randl_transaction = randl_transaction;
    }

}
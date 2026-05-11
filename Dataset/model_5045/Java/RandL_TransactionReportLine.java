





import java.util.List;
import java.util.ArrayList;

public class RandL_TransactionReportLine  {

    private String amount;
    private String serviceDesc;
    private String points;
    private String partnerName;





    private RandL_Date randl_date;




    private RandL_TransactionReport randl_transactionreport;




    private RandL_Transaction randl_transaction;




    private RandL_TransactionReport randl_transactionreport;


    public RandL_TransactionReportLine(
        String amount,        String serviceDesc,        String points,        String partnerName    ) {
        this.amount = amount;
        this.serviceDesc = serviceDesc;
        this.points = points;
        this.partnerName = partnerName;
    }


    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
    public String getServicedesc() {
        return serviceDesc;
    }

    public void setServicedesc(String serviceDesc) {
        this.serviceDesc = serviceDesc;
    }
    public String getPoints() {
        return points;
    }

    public void setPoints(String points) {
        this.points = points;
    }
    public String getPartnername() {
        return partnerName;
    }

    public void setPartnername(String partnerName) {
        this.partnerName = partnerName;
    }

    public RandL_Date getRandl_date() {
        return randl_date;
    }

    public void setRandl_date(RandL_Date randl_date) {
        this.randl_date = randl_date;
    }
    public RandL_TransactionReport getRandl_transactionreport() {
        return randl_transactionreport;
    }

    public void setRandl_transactionreport(RandL_TransactionReport randl_transactionreport) {
        this.randl_transactionreport = randl_transactionreport;
    }
    public RandL_Transaction getRandl_transaction() {
        return randl_transaction;
    }

    public void setRandl_transaction(RandL_Transaction randl_transaction) {
        this.randl_transaction = randl_transaction;
    }
    public RandL_TransactionReport getRandl_transactionreport() {
        return randl_transactionreport;
    }

    public void setRandl_transactionreport(RandL_TransactionReport randl_transactionreport) {
        this.randl_transactionreport = randl_transactionreport;
    }

}
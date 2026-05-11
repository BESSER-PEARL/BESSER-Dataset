





import java.util.List;
import java.util.ArrayList;

public class RandL_Container_RandL  {






    private List<RandL_Earning> randl_earnings;




    private List<RandL_Service> randl_services;




    private List<RandL_Membership> randl_memberships;




    private List<RandL_TransactionReport> randl_transactionreports;




    private List<RandL_TransactionReportLine> randl_transactionreportlines;




    private List<RandL_LoyaltyProgram> randl_loyaltyprograms;




    private List<RandL_ProgramPartner> randl_programpartners;




    private List<RandL_Burning> randl_burnings;




    private List<RandL_LoyaltyAccount> randl_loyaltyaccounts;




    private List<RandL_Date> randl_dates;




    private List<RandL_CustomerCard> randl_customercards;




    private List<RandL_Customer> randl_customers;




    private List<RandL_ServiceLevel> randl_servicelevels;


    public RandL_Container_RandL(
    ) {
        this.randl_earnings = new ArrayList<>();
        this.randl_services = new ArrayList<>();
        this.randl_memberships = new ArrayList<>();
        this.randl_transactionreports = new ArrayList<>();
        this.randl_transactionreportlines = new ArrayList<>();
        this.randl_loyaltyprograms = new ArrayList<>();
        this.randl_programpartners = new ArrayList<>();
        this.randl_burnings = new ArrayList<>();
        this.randl_loyaltyaccounts = new ArrayList<>();
        this.randl_dates = new ArrayList<>();
        this.randl_customercards = new ArrayList<>();
        this.randl_customers = new ArrayList<>();
        this.randl_servicelevels = new ArrayList<>();
    }

    public RandL_Container_RandL(
        ArrayList<RandL_Earning> randl_earnings,        ArrayList<RandL_Service> randl_services,        ArrayList<RandL_Membership> randl_memberships,        ArrayList<RandL_TransactionReport> randl_transactionreports,        ArrayList<RandL_TransactionReportLine> randl_transactionreportlines,        ArrayList<RandL_LoyaltyProgram> randl_loyaltyprograms,        ArrayList<RandL_ProgramPartner> randl_programpartners,        ArrayList<RandL_Burning> randl_burnings,        ArrayList<RandL_LoyaltyAccount> randl_loyaltyaccounts,        ArrayList<RandL_Date> randl_dates,        ArrayList<RandL_CustomerCard> randl_customercards,        ArrayList<RandL_Customer> randl_customers,        ArrayList<RandL_ServiceLevel> randl_servicelevels    ) {
        this.randl_earnings = randl_earnings;
        this.randl_services = randl_services;
        this.randl_memberships = randl_memberships;
        this.randl_transactionreports = randl_transactionreports;
        this.randl_transactionreportlines = randl_transactionreportlines;
        this.randl_loyaltyprograms = randl_loyaltyprograms;
        this.randl_programpartners = randl_programpartners;
        this.randl_burnings = randl_burnings;
        this.randl_loyaltyaccounts = randl_loyaltyaccounts;
        this.randl_dates = randl_dates;
        this.randl_customercards = randl_customercards;
        this.randl_customers = randl_customers;
        this.randl_servicelevels = randl_servicelevels;
    }


    public List<RandL_Earning> getRandl_earnings() {
        return randl_earnings;
    }

    public void addRandl_earning(Randl_earning randl_earning) {
        this.randl_earnings.add(randl_earning);
    }
    public List<RandL_Service> getRandl_services() {
        return randl_services;
    }

    public void addRandl_service(Randl_service randl_service) {
        this.randl_services.add(randl_service);
    }
    public List<RandL_Membership> getRandl_memberships() {
        return randl_memberships;
    }

    public void addRandl_membership(Randl_membership randl_membership) {
        this.randl_memberships.add(randl_membership);
    }
    public List<RandL_TransactionReport> getRandl_transactionreports() {
        return randl_transactionreports;
    }

    public void addRandl_transactionreport(Randl_transactionreport randl_transactionreport) {
        this.randl_transactionreports.add(randl_transactionreport);
    }
    public List<RandL_TransactionReportLine> getRandl_transactionreportlines() {
        return randl_transactionreportlines;
    }

    public void addRandl_transactionreportline(Randl_transactionreportline randl_transactionreportline) {
        this.randl_transactionreportlines.add(randl_transactionreportline);
    }
    public List<RandL_LoyaltyProgram> getRandl_loyaltyprograms() {
        return randl_loyaltyprograms;
    }

    public void addRandl_loyaltyprogram(Randl_loyaltyprogram randl_loyaltyprogram) {
        this.randl_loyaltyprograms.add(randl_loyaltyprogram);
    }
    public List<RandL_ProgramPartner> getRandl_programpartners() {
        return randl_programpartners;
    }

    public void addRandl_programpartner(Randl_programpartner randl_programpartner) {
        this.randl_programpartners.add(randl_programpartner);
    }
    public List<RandL_Burning> getRandl_burnings() {
        return randl_burnings;
    }

    public void addRandl_burning(Randl_burning randl_burning) {
        this.randl_burnings.add(randl_burning);
    }
    public List<RandL_LoyaltyAccount> getRandl_loyaltyaccounts() {
        return randl_loyaltyaccounts;
    }

    public void addRandl_loyaltyaccount(Randl_loyaltyaccount randl_loyaltyaccount) {
        this.randl_loyaltyaccounts.add(randl_loyaltyaccount);
    }
    public List<RandL_Date> getRandl_dates() {
        return randl_dates;
    }

    public void addRandl_date(Randl_date randl_date) {
        this.randl_dates.add(randl_date);
    }
    public List<RandL_CustomerCard> getRandl_customercards() {
        return randl_customercards;
    }

    public void addRandl_customercard(Randl_customercard randl_customercard) {
        this.randl_customercards.add(randl_customercard);
    }
    public List<RandL_Customer> getRandl_customers() {
        return randl_customers;
    }

    public void addRandl_customer(Randl_customer randl_customer) {
        this.randl_customers.add(randl_customer);
    }
    public List<RandL_ServiceLevel> getRandl_servicelevels() {
        return randl_servicelevels;
    }

    public void addRandl_servicelevel(Randl_servicelevel randl_servicelevel) {
        this.randl_servicelevels.add(randl_servicelevel);
    }

}






import java.util.List;
import java.util.ArrayList;

public class Company_Airport  {

    private int ticketCharges;
    private int endSchedule;
    private int beginSchedule;
    private int ticketPrice;
    private String city;





    private List<ProviderSystem_Provider> providersystem_providers;




    private Company_Company company_company;


    public Company_Airport(
        int ticketCharges,        int endSchedule,        int beginSchedule,        int ticketPrice,        String city    ) {
        this.ticketCharges = ticketCharges;
        this.endSchedule = endSchedule;
        this.beginSchedule = beginSchedule;
        this.ticketPrice = ticketPrice;
        this.city = city;
        this.providersystem_providers = new ArrayList<>();
    }

    public Company_Airport(
        int ticketCharges,        int endSchedule,        int beginSchedule,        int ticketPrice,        String city        ArrayList<ProviderSystem_Provider> providersystem_providers    ) {
        this.ticketCharges = ticketCharges;
        this.endSchedule = endSchedule;
        this.beginSchedule = beginSchedule;
        this.ticketPrice = ticketPrice;
        this.city = city;
        this.providersystem_providers = providersystem_providers;
    }

    public int getTicketcharges() {
        return ticketCharges;
    }

    public void setTicketcharges(int ticketCharges) {
        this.ticketCharges = ticketCharges;
    }
    public int getEndschedule() {
        return endSchedule;
    }

    public void setEndschedule(int endSchedule) {
        this.endSchedule = endSchedule;
    }
    public int getBeginschedule() {
        return beginSchedule;
    }

    public void setBeginschedule(int beginSchedule) {
        this.beginSchedule = beginSchedule;
    }
    public int getTicketprice() {
        return ticketPrice;
    }

    public void setTicketprice(int ticketPrice) {
        this.ticketPrice = ticketPrice;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public List<ProviderSystem_Provider> getProvidersystem_providers() {
        return providersystem_providers;
    }

    public void addProvidersystem_provider(Providersystem_provider providersystem_provider) {
        this.providersystem_providers.add(providersystem_provider);
    }
    public Company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(Company_Company company_company) {
        this.company_company = company_company;
    }

}
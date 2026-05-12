





import java.util.List;
import java.util.ArrayList;

public class Shipping_UseCase  {






    private customer_Actor customer_actor;




    private Company_Actor company_actor;


    public Shipping_UseCase(
    ) {
    }



    public customer_Actor getCustomer_actor() {
        return customer_actor;
    }

    public void setCustomer_actor(customer_Actor customer_actor) {
        this.customer_actor = customer_actor;
    }
    public Company_Actor getCompany_actor() {
        return company_actor;
    }

    public void setCompany_actor(Company_Actor company_actor) {
        this.company_actor = company_actor;
    }

}